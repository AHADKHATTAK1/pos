from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class ProductBase(BaseModel):
    business_id: str
    store_id: str
    product_name: str
    sku: Optional[str] = None
    barcode: Optional[str] = None
    category: Optional[str] = None
    price: float
    stock: int = 0
    stock_threshold: int = 5
    supplier_id: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class ProductResponse(BaseModel):
    id: str
    business_id: str
    store_id: str
    product_name: str
    sku: Optional[str] = None
    barcode: Optional[str] = None
    category: Optional[str] = None
    price: float
    stock: int
    stock_threshold: int
    supplier_id: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
