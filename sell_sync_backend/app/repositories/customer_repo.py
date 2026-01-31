from app.core.database import get_database
from app.models.customer import CustomerInDB
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Optional
from bson import ObjectId

async def get_customer_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["customers"]

async def create_customer(customer_in: CustomerInDB):
    collection = await get_customer_collection()
    customer_dict = customer_in.dict(by_alias=True)
    await collection.insert_one(customer_dict)
    return customer_in

async def get_customers_by_business(business_id: str) -> List[CustomerInDB]:
    collection = await get_customer_collection()
    cursor = collection.find({"business_id": business_id})
    customers = []
    async for customer in cursor:
        customers.append(CustomerInDB(**customer))
    return customers

async def update_loyalty_points(customer_id: str, points: int):
    collection = await get_customer_collection()
    await collection.update_one(
        {"_id": ObjectId(customer_id)},
        {"$inc": {"loyalty_points": points}}
    )
