import streamlit as st
import requests as rq
from dotenv import load_dotenv
import os
import json
import datetime

file_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(file_path, "config.env")
json_path = os.path.join(file_path, "modelos.json")
hist_path = os.path.join(file_path, 'hist.txt')
load_dotenv(config_path)

with open(json_path, 'r') as j:
    list_models = json.load(j)

def limpar_chat():
    st.session_state["lista_mensagens"] = []
    if "contexto_adicionado" in st.session_state: 
        del st.session_state["contexto_adicionado"]
        with open(hist_path, 'a') as H:
            print("=" * 50, file= H)

def context_system():
    contexto = st.text_area("insira um contexto(opcional)")
    usar_contexto = st.checkbox("Usar Contexto do sistema")
    return contexto, usar_contexto

api_key = os.getenv("Api_key")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
#["nenhum" ,"Deep Seek", "Mistral Small", "Llama 3.1"]
with st.sidebar:
    st.write("Configurações")
    caixa_de_selecao = st.selectbox("escolha o modelo de ia", list_models.keys())

    if caixa_de_selecao != "nenhum":
        contexto, usar_contexto = context_system()
        if usar_contexto and contexto.strip() and "contexto_adicionado" not in st.session_state: 
            st.session_state["lista_mensagens"].append({"role": "system", "content": contexto}) 
            st.session_state["contexto_adicionado"] = True
            with open(hist_path, 'a') as H:
                print(f"System: {contexto}\n", file= H)
        limpar = st.button('Limpar')
        if limpar:
            limpar_chat()

if caixa_de_selecao != "nenhum":
    mensagem_usuario = st.chat_input("Digite sua mensagem")
    
    

    for mensagem in st.session_state["lista_mensagens"]:
        st.chat_message(mensagem["role"]).write(mensagem["content"])

    if mensagem_usuario:
        st.chat_message("user").write(mensagem_usuario)
        mensagem_user = {"role": "user", "content": mensagem_usuario}
        st.session_state["lista_mensagens"].append(mensagem_user)
        with open(hist_path, 'a') as H:
            print(f'User: {mensagem_user["content"]}\n', file= H)
    try:
        with st.spinner("Pensando..."):
            resposta_ia = rq.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={ 
                    "Authorization": f"Bearer {api_key}", 
                    "Content-Type": "application/json" 
                },
                json={
                    "model": list_models[caixa_de_selecao],
                    "messages": st.session_state["lista_mensagens"]
                    }
                ).json()
            texto_resposta_ia = resposta_ia["choices"][0]["message"]["content"]
            
            st.chat_message("assistant").write(texto_resposta_ia)
            mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
            st.session_state["lista_mensagens"].append(mensagem_ia)

            with open(hist_path, 'a') as H:
                print(f'Assistant: {resposta_ia["choices"][0]["message"]["content"]}\n', file= H)
                dia = datetime.datetime.now().time()
                print(dia)
                print(f'Assistant: {resposta_ia}')

            if len(st.session_state["lista_mensagens"]) > 20:  # Mantém as últimas 20 interações
                st.session_state["lista_mensagens"] = st.session_state["lista_mensagens"][-20:]

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
