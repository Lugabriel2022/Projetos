import requests as rq
import asyncio
import json
import time
from dotenv import load_dotenv
import os

class Funcs():
    file_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(file_path, "config.env")
    load_dotenv(config_path)
    api_key = os.getenv("Api_key")
    cache_chat = []
    def limpar(self):
        self.txt_chat.configure(state='normal')
        self.txt_chat.delete('1.0', 'end')
        self.txt_chat.configure(state='disabled')
        self.bt_enviar.configure(state= 'normal')
        self.cache_chat = []

    def mensagem_usuario(self):
        self.txt_chat.configure(state='normal')
        mensagem = self.txt_mensagem.get("1.0", "end-1c")
        mensagem_chat = {
            "role": "user", "content": mensagem
        }
        self.txt_chat.insert("end", f"user: {mensagem}\n\n")
        self.cache_chat.append(mensagem_chat)
        self.txt_chat.configure(state='disabled')
        self.bt_enviar.configure(state= 'disabled')
        self.txt_mensagem.delete('1.0', 'end')
        self.janela.after(100, resposta_ia())

    def context_system(self):
        mensagem = self.txt_contest.get("1.0", "end-1c")
        mensagem_chat = {
            "role": "system", "content": mensagem
        }
        self.cache_chat.append(mensagem_chat)
        self.txt_chat.configure(state='normal')
        self.txt_chat.insert("end", f"system: {mensagem}\n\n")        
        self.txt_chat.configure(state= 'disabled')



    def resposta_ia(self, tentativas=0, max_tentativas=15):
        try:
            resposta = rq.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.models[self.cb_modelo.get()],
                    "messages": self.cache_chat
                },
                timeout=30
            )

            # 1. Se a API deu erro real (404, 429, 500 etc.)
            if resposta.status_code != 200:
                self.txt_chat.configure(state="normal")
                self.txt_chat.insert("end", f"Erro da API: {resposta.status_code}\n\n")
                self.txt_chat.configure(state="disabled")
                self.bt_enviar.configure(state="normal")
                return

            # 2. Se status 200, checa o JSON
            resposta_ia = resposta.json()
            if "choices" in resposta_ia and resposta_ia["choices"]:
                conteudo = resposta_ia["choices"][0]["message"]["content"]
                self.txt_chat.configure(state="normal")
                self.txt_chat.insert("end", f"Bot: {conteudo}\n\n")
                self.cache_chat.append({"role": "assistant", "content": conteudo})
                self.txt_chat.configure(state="disabled")
                self.bt_enviar.configure(state="normal")
            else:
                # 3. Resposta incompleta → re-tenta com after
                if tentativas < max_tentativas:
                    self.txt_chat.configure(state="normal")
                    self.txt_chat.insert("end", "Ainda aguardando resposta da IA...\n")
                    self.txt_chat.configure(state="disabled")
                    self.janela.after(2000, lambda: self.resposta_ia(tentativas+1, max_tentativas))
                else:
                    self.txt_chat.configure(state="normal")
                    self.txt_chat.insert("end", "Erro: resposta não recebida dentro do tempo limite\n\n")
                    self.txt_chat.configure(state="disabled")
                    self.bt_enviar.configure(state="normal")

        except Exception as e:
            self.txt_chat.configure(state="normal")
            self.txt_chat.insert("end", f"Erro na resposta da IA: {e}\n\n")
            self.txt_chat.configure(state="disabled")
            self.bt_enviar.configure(state="normal")

        if len(self.cache_chat) >= 30:
            self.cache_chat = self.cache_chat[-30:]
