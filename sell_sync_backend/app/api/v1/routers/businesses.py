from fastapi import APIRouter, HTTPException, status, Depends
from app.models.business import BusinessCreate, BusinessInDB, BusinessResponse
from app.repositories import business_repo
from app.core.utils import generate_api_key

router = APIRouter()

@router.post("/", response_model=BusinessResponse)
async def create_business(business_in: BusinessCreate):
    existing_business = await business_repo.get_business_by_owner(business_in.business_owner)
    if existing_business:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Business already exists for this owner"
        )
    
    api_key = generate_api_key()
    business_db = BusinessInDB(
        **business_in.dict(),
        api_key=api_key
    )
    
    await business_repo.create_business(business_db)
    return BusinessResponse(id=str(business_db.id), **business_db.dict())

@router.get("/me", response_model=BusinessResponse)
async def get_my_business(owner_id: str):
    business = await business_repo.get_business_by_owner(owner_id)
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found"
        )
    return BusinessResponse(id=str(business.id), **business.dict())
