from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

# Criação do engine para o PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Criar a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
