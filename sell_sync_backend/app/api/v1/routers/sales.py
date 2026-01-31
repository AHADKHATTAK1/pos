from fastapi import APIRouter, HTTPException, status, Depends
from app.models.sale import SaleCreate, SaleResponse, SaleInDB
from app.repositories import sale_repo, product_repo, customer_repo
from typing import List

router = APIRouter()

@router.post("/", response_model=SaleResponse)
async def create_sale(sale_in: SaleCreate):
    # 1. Update stock for each item
    for item in sale_in.items:
        await product_repo.update_stock(item.product_id, -item.quantity)
    
    # 2. Update loyalty points if customer exists (e.g., 1 point per $10)
    if sale_in.customer_id:
        points = int(sale_in.total_amount // 10)
        await customer_repo.update_loyalty_points(sale_in.customer_id, points)
    
    sale_db = SaleInDB(**sale_in.dict())
    await sale_repo.create_sale(sale_db)
    return SaleResponse(id=str(sale_db.id), **sale_db.dict())

@router.get("/{store_id}", response_model=List[SaleResponse])
async def get_sales(store_id: str):
    sales = await sale_repo.get_sales_by_store(store_id)
    return [SaleResponse(id=str(s.id), **s.dict()) for s in sales]
