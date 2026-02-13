import customtkinter as ctk
from tkinter import PhotoImage
from funcs import *
import os
import json

os.system('clear')

class Bot_app(Funcs):
    """
    Classe principal do chatbot com interface gráfica em CustomTkinter.
    Herda funções auxiliares da classe Funcs.
    """

    # Caminhos de arquivos importantes
    file_path = os.path.dirname(os.path.abspath(__file__))  # pasta atual do script
    json_path = os.path.join(file_path, 'modelos.json')     # arquivo de modelos
    icone_path = os.path.join(file_path, 'assets', 'Chat_ai_icon.png')  # ícone da janela

    # Carrega os modelos disponíveis do arquivo JSON
    with open(json_path, 'r') as j:
        models = json.load(j)
    list_models = list(models.keys())

    def __init__(self):
        """Inicializa a janela principal e configura os elementos da interface."""
        self.janela = ctk.CTk()
        self.icone = PhotoImage(file=self.icone_path)  # carrega o ícone da janela

        # Configurações e widgets
        self.config_tela()
        self.telas()
        self.widgets_tela_chat()
        self.widgets_tela_configs()
        self.widgets_tela_entrada()

        # Loop principal da interface
        self.janela.mainloop()

    def config_tela(self):
        """Configura tamanho, título, redimensionamento e ícone da janela."""
        self.janela.geometry("700x800")
        self.janela.title("Chatbot inicial")
        self.janela.resizable(False, False)
        self.janela.iconphoto(False, self.icone)

    def telas(self):
        """Cria e posiciona os frames principais da interface (chat, entrada e configs)."""
        self.tela_chat = ctk.CTkFrame(self.janela)
        self.tela_entrada = ctk.CTkFrame(self.janela)
        self.tela_configs = ctk.CTkFrame(self.janela)

        # posicionamento dos frames
        self.tela_chat.place(relx=0.01, rely=0.01, relwidth=0.68, relheight=0.8)
        self.tela_configs.place(relx=0.7, rely=0.01, relwidth=0.29, relheight=0.8)
        self.tela_entrada.place(relx=0.01, rely=0.82, relwidth=0.98, relheight=0.17)

    def widgets_tela_chat(self):
        """Cria a área de texto para exibir o histórico de mensagens do chat."""
        self.txt_chat = ctk.CTkTextbox(self.tela_chat, state="disabled")
        self.txt_chat.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_tela_configs(self):
        """Cria os widgets da tela de configurações (contexto, modelos, limpar)."""
        self.lb_contest = ctk.CTkLabel(self.tela_configs, text='Contexto (opcional)', anchor="center")
        self.txt_contest = ctk.CTkTextbox(self.tela_configs)
        self.bt_contest = ctk.CTkButton(self.tela_configs, text='Usar contexto', command=self.context_system)
        self.cb_modelo = ctk.CTkComboBox(self.tela_configs, values=self.list_models)
        self.bt_limpar = ctk.CTkButton(self.tela_configs, text='Limpar', command=self.limpar)

        # posicionamento dos widgets
        self.lb_contest.place(relx=0.25, rely=0.01)
        self.txt_contest.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.2)
        self.bt_contest.place(relx=0.02, rely=0.26, relwidth=0.96, relheight=0.05)
        self.cb_modelo.place(relx=0.02, rely=0.33, relwidth=0.96, relheight=0.06)
        self.bt_limpar.place(relx=0.02, rely=0.41, relwidth=0.3, relheight=0.05)

    def widgets_tela_entrada(self):
        """Cria a área de entrada de mensagem e botão de envio."""
        self.txt_mensagem = ctk.CTkTextbox(self.tela_entrada)
        self.bt_enviar = ctk.CTkButton(self.tela_entrada, text='Enviar', command=self.mensagem_usuario)

        # posicionamento
        self.txt_mensagem.place(relx=0.02, rely=0.25, relwidth=0.76, relheight=0.25)
        self.bt_enviar.place(relx=0.79, rely=0.25, relwidth=0.18, relheight=0.25)


# Executa o aplicativo
Bot_app()
