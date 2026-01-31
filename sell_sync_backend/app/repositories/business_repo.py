from app.core.database import get_database
from app.models.business import BusinessInDB
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List

async def get_business_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["businesses"]

async def create_business(business_in: BusinessInDB):
    collection = await get_business_collection()
    business_dict = business_in.dict(by_alias=True)
    await collection.insert_one(business_dict)
    return business_in

async def get_business_by_owner(owner_id: str):
    collection = await get_business_collection()
    business = await collection.find_one({"business_owner": owner_id})
    if business:
        return BusinessInDB(**business)
    return None

async def get_business_by_api_key(api_key: str):
    collection = await get_business_collection()
    business = await collection.find_one({"api_key": api_key})
    if business:
        return BusinessInDB(**business)
    return None
