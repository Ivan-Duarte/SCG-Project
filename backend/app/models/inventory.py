from sqlalchemy import Column, Integer, String, Float
from ..db.base import Base

class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    category = Column(String, nullable=False)
    stock_quantity = Column(Integer, default=0)
    location = Column(String, nullable=True)
    general_info = Column(String, nullable=True)
