from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate
from app.services.inventory_service import create_inventory_item_service, delete_inventory_item_service, update_inventory_item_service, get_inventory_items_service, get_inventory_item_by_id_service

router = APIRouter()

@router.post("/", response_model=InventoryItemCreate)
def create_inventory_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    try:
        # Aqui, o controller chama a função de serviço, delegando a lógica de criação ao serviço
        return create_inventory_item_service(item, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{item_id}", status_code=200)
def delete_inventory_item(item_id: int, db: Session = Depends(get_db)):
    return delete_inventory_item_service(item_id, db)

@router.put("/{item_id}", status_code=200)
def update_inventory_item(item_id: int, item_update: InventoryItemUpdate, db: Session = Depends(get_db)):
    return update_inventory_item_service(item_id, item_update, db)

# Rota para buscar todos os itens do inventário
@router.get("/", response_model=list[InventoryItemCreate])
def get_inventory_items(db: Session = Depends(get_db)):
    return get_inventory_items_service(db)

# Rota para buscar um item específico pelo ID
@router.get("/{item_id}", response_model=InventoryItemCreate)
def get_inventory_item_by_id(item_id: int, db: Session = Depends(get_db)):
    return get_inventory_item_by_id_service(item_id, db)
