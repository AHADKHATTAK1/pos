from fastapi import APIRouter, HTTPException, status, Depends
from app.models.customer import CustomerCreate, CustomerResponse, CustomerInDB
from app.repositories import customer_repo
from typing import List

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
async def create_customer(customer_in: CustomerCreate):
    customer_db = CustomerInDB(**customer_in.dict())
    await customer_repo.create_customer(customer_db)
    return CustomerResponse(id=str(customer_db.id), **customer_db.dict())

@router.get("/{business_id}", response_model=List[CustomerResponse])
async def get_customers(business_id: str):
    customers = await customer_repo.get_customers_by_business(business_id)
    return [CustomerResponse(id=str(c.id), **c.dict()) for c in customers]
