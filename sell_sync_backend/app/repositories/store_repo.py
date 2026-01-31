from app.core.database import get_database
from app.models.store import StoreInDB
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List

async def get_store_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["stores"]

async def create_store(store_in: StoreInDB):
    collection = await get_store_collection()
    store_dict = store_in.dict(by_alias=True)
    await collection.insert_one(store_dict)
    return store_in

async def get_stores_by_business(business_id: str) -> List[StoreInDB]:
    collection = await get_store_collection()
    cursor = collection.find({"business_id": business_id})
    stores = []
    async for store in cursor:
        stores.append(StoreInDB(**store))
    return stores
