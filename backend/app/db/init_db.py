from .session import engine
from ..models import inventory

def init_db():
    inventory.Base.metadata.create_all(bind=engine)
