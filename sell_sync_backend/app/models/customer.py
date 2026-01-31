from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class CustomerBase(BaseModel):
    business_id: str
    name: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    loyalty_points: int = 0

class CustomerCreate(CustomerBase):
    pass

class CustomerInDB(CustomerBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class CustomerResponse(BaseModel):
    id: str
    business_id: str
    name: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    loyalty_points: int
    created_at: datetime

    class Config:
        from_attributes = True
