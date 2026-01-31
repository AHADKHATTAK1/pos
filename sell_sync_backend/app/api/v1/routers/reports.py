from fastapi import APIRouter, Depends
from app.services import report_service

router = APIRouter()

@router.get("/{business_id}")
async def get_report(business_id: str):
    return await report_service.generate_business_report(business_id)
