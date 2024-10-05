from pydantic import BaseModel
from typing import Optional

class InventoryItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    stock_quantity: Optional[int] = 0
    location: Optional[str] = None
    general_info: Optional[str] = None

class InventoryItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    stock_quantity: Optional[int] = None
    location: Optional[str] = None
    general_info: Optional[str] = None