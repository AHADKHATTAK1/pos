from app.repositories import sale_repo, product_repo, customer_repo
from typing import Dict

async def generate_business_report(business_id: str) -> Dict:
    # A simple report aggregator
    # In a real app, this would use MongoDB aggregation pipelines
    sales = await sale_repo.get_sales_by_store(business_id) # Should be by business
    total_revenue = sum(sale.total_amount for sale in sales)
    total_sales_count = len(sales)
    
    return {
        "business_id": business_id,
        "total_revenue": total_revenue,
        "total_sales_count": total_sales_count,
        "report_generated_at": str(datetime.utcnow())
    }
from datetime import datetime
