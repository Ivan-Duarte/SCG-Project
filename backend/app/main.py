from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import environ as env
from dotenv import load_dotenv
import os
from .api.routes import inventory_controller  # Importando os endpoints
from .db.init_db import init_db

# Carregar o arquivo .env
load_dotenv()

init_db()

app = FastAPI()

allowed_origins = env.get("ALLOWED_ORIGINS")
origins = allowed_origins.split(",") if allowed_origins else []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir o roteamento do inventário
app.include_router(inventory_controller.router, prefix="/items", tags=["Rotas de Itens"])

@app.get("/status")
def get_status():
    return {"status": "ok", "message": f"Backend está funcionando corretamente! Instância: {env.get('INSTANCE_ID', 'Indefinido')}"}