from fastapi import APIRouter, HTTPException, status, Depends
from app.models.store import StoreCreate, StoreInDB, StoreResponse
from app.repositories import store_repo
from typing import List

router = APIRouter()

@router.post("/", response_model=StoreResponse)
async def create_store(store_in: StoreCreate):
    store_db = StoreInDB(**store_in.dict())
    await store_repo.create_store(store_db)
    return StoreResponse(id=str(store_db.id), **store_db.dict())

@router.get("/{business_id}", response_model=List[StoreResponse])
async def get_stores(business_id: str):
    stores = await store_repo.get_stores_by_business(business_id)
    return [StoreResponse(id=str(s.id), **s.dict()) for s in stores]
