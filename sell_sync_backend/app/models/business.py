from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class BusinessSettings(BaseModel):
    currency: str = "USD"
    timezone: str = "UTC"
    tax_inclusive: bool = True

class BusinessBase(BaseModel):
    business_name: str
    business_owner: str # User ID
    package_plan: str = "Free" # Free, Standard, Premium
    subscription_status: str = "active"

class BusinessCreate(BusinessBase):
    pass

class BusinessInDB(BusinessBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    api_key: str
    settings: BusinessSettings = Field(default_factory=BusinessSettings)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class BusinessResponse(BaseModel):
    id: str
    business_name: str
    business_owner: str
    package_plan: str
    subscription_status: str
    api_key: str
    settings: BusinessSettings
    created_at: datetime

    class Config:
        from_attributes = True
