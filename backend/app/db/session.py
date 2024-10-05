from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings
from contextlib import contextmanager

# Criação do engine para o PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Criar a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função que gerencia a criação e o fechamento da sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

