from fastapi import APIRouter, HTTPException, status, Depends
from app.models.product import ProductCreate, ProductResponse, ProductInDB
from app.repositories import product_repo
from typing import List

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def create_product(product_in: ProductCreate):
    product_db = ProductInDB(**product_in.dict())
    await product_repo.create_product(product_db)
    return ProductResponse(id=str(product_db.id), **product_db.dict())

@router.get("/{store_id}", response_model=List[ProductResponse])
async def get_products(store_id: str):
    products = await product_repo.get_products_by_store(store_id)
    return [ProductResponse(id=str(p.id), **p.dict()) for p in products]

@router.patch("/{product_id}/stock")
async def update_stock(product_id: str, quantity: int):
    await product_repo.update_stock(product_id, quantity)
    return {"message": "Stock updated successfully"}
