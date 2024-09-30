from fastapi import FastAPI
from os import environ as env
from dotenv import load_dotenv
import os

# Carregar o arquivo .env
load_dotenv()

app = FastAPI()

@app.get("/")
def index():
    return {"details": f"Hello, World! Senha de Ambiente = {env.get('MY_VARIABLE', 'Não encontrada')}"}