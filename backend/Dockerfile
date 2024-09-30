# backend/Dockerfile

# Usar uma imagem base mais abrangente do Python para evitar problemas de compatibilidade
FROM python:3.10 AS backend

# Configurar o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para o container e instalar as dependências
COPY requirements.txt .

# Instalar as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação para o container
COPY . .

# Expor a porta 8000 para acessar o FastAPI
EXPOSE 8000

# Comando para rodar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
