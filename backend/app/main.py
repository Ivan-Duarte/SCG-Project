from fastapi import FastAPI
from os import environ as env
from dotenv import load_dotenv
import os
from .api.routes import inventory_controller  # Importando os endpoints
from .db.init_db import init_db

# Carregar o arquivo .env
load_dotenv()


init_db()

app = FastAPI()

# Incluir o roteamento do inventário
app.include_router(inventory_controller.router, prefix="/items", tags=["Rotas de Itens"])

@app.get("/")
def index():
    return {"details": f"Hello, World! Senha de Ambiente = {env.get('MY_VARIABLE', 'Não encontrada')}"}