import requests as rq
import json
import os
from dotenv import load_dotenv
import threading

class Funcs:
    """
    Classe que contém as funções auxiliares do chatbot.
    Responsável por limpar o chat, enviar mensagens do usuário,
    aplicar contexto do sistema e obter respostas da IA via API OpenRouter.
    """

    # Caminhos e configuração inicial
    file_path = os.path.dirname(os.path.abspath(__file__))  # pasta atual do script
    config_path = os.path.join(file_path, "config.env")     # arquivo de configuração
    load_dotenv(config_path)                                # carrega variáveis de ambiente
    api_key = os.getenv("Api_key")                          # chave da API
    cache_chat = []                                         # histórico de mensagens (máx. 30)

    def desbloquear_envio(self, choice):
        """mantem o botão enviar bloqueado enquanto um modelo não for selecionado"""
        if choice != 'nenhum': # se o usuário escolheu algum modelo 
            self.bt_enviar.configure(state="normal") 
        else: 
            self.bt_enviar.configure(state="disabled")

    def limpar(self):
        """Limpa o histórico do chat e reseta o estado dos widgets."""
        self.txt_chat.configure(state='normal')
        self.txt_chat.delete('1.0', 'end')
        self.txt_chat.configure(state='disabled')
        self.bt_enviar.configure(state='normal')
        self.cache_chat = []

    def mensagem_usuario(self):
        """Captura a mensagem do usuário, adiciona ao cache e agenda resposta da IA."""
        self.txt_chat.configure(state='normal')
        mensagem = self.txt_mensagem.get("1.0", "end-1c")
        mensagem_chat = {"role": "user", "content": mensagem}

        # exibe mensagem do usuário no chat
        self.txt_chat.insert("end", f"user: {mensagem}\n\n", "user")
        self.cache_chat.append(mensagem_chat)

        # desabilita entrada até resposta da IA
        self.txt_chat.configure(state='disabled')
        self.bt_enviar.configure(state='disabled')
        self.txt_mensagem.delete('1.0', 'end')

        # agenda chamada da IA (after evita travar interface)
        self.janela.after(100, self.resposta_ia)

    def context_system(self):
        """Adiciona contexto opcional do sistema ao cache e exibe no chat."""
        mensagem = self.txt_contest.get("1.0", "end-1c")
        mensagem_chat = {"role": "system", "content": mensagem,}
        self.cache_chat.append(mensagem_chat)

        self.txt_chat.configure(state='normal')
        self.txt_chat.insert("end", f"system: {mensagem}\n\n", "system")
        self.txt_chat.configure(state='disabled')
        self.resposta_ia()

    def resposta_ia(self, tentativas=0, max_tentativas=15):
        """
        Envia o histórico de mensagens para a API OpenRouter e processa a resposta.
        Executa em uma thread separada para não travar a interface.
        """
        def tarefa():
            modelo = self.cb_modelo.get()
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

                if resposta.status_code != 200:
                    self.txt_chat.configure(state="normal")
                    self.txt_chat.insert("end", f"Erro da API: {resposta.status_code}\n\n")
                    self.txt_chat.configure(state="disabled")
                    self.bt_enviar.configure(state="normal")
                    return

                resposta_ia = resposta.json()
                if "choices" in resposta_ia and resposta_ia["choices"]:
                    conteudo = resposta_ia["choices"][0]["message"]["content"]
                    self.txt_chat.configure(state="normal")
                    self.txt_chat.insert("end", f"Bot: {conteudo}\n\n", "bot")
                    self.cache_chat.append({"role": "assistant", "content": conteudo})
                    self.txt_chat.configure(state="disabled")
                    self.bt_enviar.configure(state="normal")
                else:
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

        # cria e inicia a thread
        threading.Thread(target=tarefa).start()

