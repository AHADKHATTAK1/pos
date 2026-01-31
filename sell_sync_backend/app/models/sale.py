from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class SaleItem(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    total_price: float

class SaleBase(BaseModel):
    business_id: str
    store_id: str
    cashier_id: str
    customer_id: Optional[str] = None
    items: List[SaleItem]
    payment_method: str = "Cash"
    total_amount: float
    tax_amount: float = 0.0
    transaction_status: str = "completed"

class SaleCreate(SaleBase):
    pass

class SaleInDB(SaleBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class SaleResponse(BaseModel):
    id: str
    business_id: str
    store_id: str
    cashier_id: str
    items: List[SaleItem]
    payment_method: str
    total_amount: float
    transaction_status: str
    created_at: datetime

    class Config:
        from_attributes = True
