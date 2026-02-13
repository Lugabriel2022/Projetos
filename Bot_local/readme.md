# Chatbot Local

Um chatbot simples em Python com interface em **CustomTkinter**, utilizando modelos da [OpenRouter](https://openrouter.ai).

---

## 🚀 Como usar

1. **Crie uma conta no OpenRouter**  
   Acesse [https://openrouter.ai](https://openrouter.ai) e faça seu cadastro.

2. **Obtenha sua API Key**  
   - Após o login, clique em **Get API Key**.  
   - Isso abrirá a página de **Keys** da sua conta.  
   - Clique em **Create** e preencha apenas o nome (opcional).  
   - Confirme em **Create** para gerar a chave.

3. **Configure o arquivo `config.env`**  
   - Copie a chave gerada.  
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
