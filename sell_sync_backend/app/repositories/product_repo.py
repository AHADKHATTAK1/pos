from app.core.database import get_database
from app.models.product import ProductInDB
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Optional
from bson import ObjectId

async def get_product_collection() -> AsyncIOMotorCollection:
    db = await get_database()
    return db["products"]

async def create_product(product_in: ProductInDB):
    collection = await get_product_collection()
    product_dict = product_in.dict(by_alias=True)
    await collection.insert_one(product_dict)
    return product_in

async def get_products_by_store(store_id: str) -> List[ProductInDB]:
    collection = await get_product_collection()
    cursor = collection.find({"store_id": store_id})
    products = []
    async for product in cursor:
        products.append(ProductInDB(**product))
    return products

async def update_stock(product_id: str, quantity_change: int):
    collection = await get_product_collection()
    await collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$inc": {"stock": quantity_change}}
    )
