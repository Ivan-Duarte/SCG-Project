from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate
from app.models.inventory import InventoryItem

#Função que cria novos itens no BD
def create_inventory_item_service(item: InventoryItemCreate, db: Session):
    # Lógica de negócios para criar um item no inventário
    db_item = InventoryItem(
        name=item.name,
        description=item.description,
        category=item.category,
        stock_quantity=item.stock_quantity,
        location=item.location,
        general_info=item.general_info
    )
    
    # Adicionar o item ao banco de dados
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

#Função que exclui um item no BD
def delete_inventory_item_service(item_id: int, db: Session):
    # Buscar o item pelo ID no banco de dados
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    
    # Verificar se o item existe
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    # Remover o item do banco de dados
    db.delete(db_item)
    db.commit()

    return {"detail": "Item excluido com sucesso!"}

#Função para atualizar um item no BD
def update_inventory_item_service(item_id: int, item_update: InventoryItemUpdate, db: Session):
    # Buscar o item pelo ID no banco de dados
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    
    # Verificar se o item existe
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    # Atualizar os campos do item
    update_data = item_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    # Confirmar a atualização no banco de dados
    db.commit()
    db.refresh(db_item)

    return db_item

def get_inventory_items_service(db: Session):
    return db.query(InventoryItem).all()

def get_inventory_item_by_id_service(item_id: int, db: Session):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item