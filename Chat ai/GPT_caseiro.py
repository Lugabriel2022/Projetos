import streamlit as st
import requests as rq
from dotenv import load_dotenv
import os
import json

file_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(file_path, "config.env")
load_dotenv(config_path)

def limpar_chat():
    st.session_state["lista_mensagens"] = []
    if "contexto_adicionado" in st.session_state: 
        del st.session_state["contexto_adicionado"]

def context_system():
    contexto = st.text_area("insira um contexto(opcional)")
    usar_contexto = st.checkbox("Usar Contexto do sistema")
    return contexto, usar_contexto

api_key = os.getenv("Api_key")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

with st.sidebar:
    st.write("Configurações")
    caixa_de_selecao = st.selectbox("escolha o modelo de ia", ["nenhum" ,"Deep Seek", "Mimo-v2"])
    modelos = {"Deep Seek": "tngtech/deepseek-r1t2-chimera:free", "Mimo-v2" : "xiaomi/mimo-v2-flash"}
    if caixa_de_selecao != "nenhum":
        contexto, usar_contexto = context_system()
        if usar_contexto and contexto.strip() and "contexto_adicionado" not in st.session_state: 
            st.session_state["lista_mensagens"].append({"role": "system", "content": contexto}) 
            st.session_state["contexto_adicionado"] = True
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

        resposta_ia = rq.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={ 
                "Authorization": f"Bearer {api_key}", 
                "Content-Type": "application/json" 
            },
            json={
                "model": modelos[caixa_de_selecao],
                "messages": st.session_state["lista_mensagens"]
            }
        ).json()
        texto_resposta_ia = resposta_ia["choices"][0]["message"]["content"]
        print(resposta_ia)
        st.chat_message("assistant").write(texto_resposta_ia)
        mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)

        if len(st.session_state["lista_mensagens"]) > 20:  # Mantém as últimas 20 interações
            st.session_state["lista_mensagens"] = st.session_state["lista_mensagens"][-20:]