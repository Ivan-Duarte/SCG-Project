from sqlalchemy import inspect
from .session import engine
from ..models import inventory

def init_db():
    inspector = inspect(engine)
    tables = ['inventory_items']  # Lista de todas as suas tabelas

    for table in tables:
        if not inspector.has_table(table):
            print(f"Tabela {table} não existe. Criando tabela...")
            inventory.Base.metadata.create_all(bind=engine)
        else:
            print(f"Tabela {table} já existe. Nenhuma ação necessária.")