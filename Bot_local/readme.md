# 🤖 Chatbot Local com CustomTkinter

Este projeto é um **chatbot em Python** com interface gráfica feita em **CustomTkinter**, integrado à [OpenRouter](https://openrouter.ai).  
Ele foi desenvolvido para estudo e prática de integração de APIs, interface gráfica e boas práticas de organização de código.

---

## 🛠️ Requisitos

- Python 3.10+  
- Bibliotecas necessárias:
  - `customtkinter`
  - `requests`
  - `python-dotenv`

### Instalando bibliotecas
```bash
pip install customtkinter requests python-dotenv

---

## 📂 Estrutura do projeto

Bot_local/
│
├── Interface.py      # Interface gráfica (CustomTkinter)
├── Funcs.py          # Funções auxiliares (requisições, cache, etc.)
├── config.env        # Configuração da API Key
├── modelos.json      # Lista de modelos disponíveis
└── assets/           # Ícones e recursos visuais

---

## 🚀 Como usar

1. **Crie uma conta no OpenRouter**  
   Acesse [https://openrouter.ai](https://openrouter.ai) e faça seu cadastro.

2. **Obtenha sua API Key**  
   - Após o login, clique em **Get API Key**.  
   - Isso abrirá a página de **Keys** da sua conta.  
   - Clique em **Create**, dê um nome (opcional) e confirme.  
   - Copie a chave gerada.

3. **Configure o arquivo `config.env`**  
   - Abra o arquivo `config.env`.  
   - Substitua o texto `"Insira a chave de api aqui"` pela sua chave.  
   - **Importante:** mantenha as aspas.

4. **Gerencie os modelos (`modelos.json`)**  
   - O arquivo já traz alguns modelos gratuitos para teste.  
   - Para **remover** um modelo, basta apagar a linha correspondente.  
   - Para **adicionar** um novo, siga o formato:  
     ```json
     "nome_do_modelo": "link_do_modelo",
     ```
     > Lembre-se de colocar uma vírgula no modelo anterior ao que você adicionou.

   **Exemplo:**
   ```json
   "Deep Seek": "tngtech/deepseek-r1t2-chimera:free"
