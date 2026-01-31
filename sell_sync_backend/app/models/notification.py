from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class NotificationBase(BaseModel):
    business_id: str
    store_id: Optional[str] = None
    user_id: Optional[str] = None
    message: str
    status: str = "unread"

class NotificationCreate(NotificationBase):
    pass

class NotificationInDB(NotificationBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class NotificationResponse(BaseModel):
    id: str
    message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
