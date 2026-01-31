from app.core.database import get_database
from app.models.sale import SaleInDB
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List

async def get_sale_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["sales"]

async def create_sale(sale_in: SaleInDB):
    collection = await get_sale_collection()
    sale_dict = sale_in.dict(by_alias=True)
    await collection.insert_one(sale_dict)
    return sale_in

async def get_sales_by_store(store_id: str) -> List[SaleInDB]:
    collection = await get_sale_collection()
    cursor = collection.find({"store_id": store_id})
    sales = []
    async for sale in cursor:
        sales.append(SaleInDB(**sale))
    return sales
