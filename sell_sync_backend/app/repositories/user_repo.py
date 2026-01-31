from app.core.database import get_database
from app.models.user import UserInDB
from motor.motor_asyncio import AsyncIOMotorCollection

async def get_user_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["users"]

async def create_user(user_in: UserInDB):
    collection = await get_user_collection()
    user_dict = user_in.dict(by_alias=True)
    await collection.insert_one(user_dict)
    return user_in

async def get_user_by_email(email: str):
    collection = await get_user_collection()
    user = await collection.find_one({"email": email})
    if user:
        return UserInDB(**user)
    return None
