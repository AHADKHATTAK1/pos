from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class OperatingHours(BaseModel):
    open: str = "09:00 AM"
    close: str = "06:00 PM"

class StoreBase(BaseModel):
    business_id: str
    store_name: str
    location: Optional[str] = None
    phone: Optional[str] = None
    operating_hours: OperatingHours = Field(default_factory=OperatingHours)

class StoreCreate(StoreBase):
    pass

class StoreInDB(StoreBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class StoreResponse(BaseModel):
    id: str
    business_id: str
    store_name: str
    location: Optional[str] = None
    phone: Optional[str] = None
    operating_hours: OperatingHours
    created_at: datetime

    class Config:
        from_attributes = True
