from fastapi import FastAPI
from app.core.database import connect_to_mongo, close_mongo_connection
from app.core.logging import global_exception_handler, logger
from app.api.v1.routers import auth, businesses, stores, inventory, sales, customers, reports

app = FastAPI(title="Sell Sync POS API")

app.add_exception_handler(Exception, global_exception_handler)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(businesses.router, prefix="/api/v1/businesses", tags=["businesses"])
app.include_router(stores.router, prefix="/api/v1/stores", tags=["stores"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["inventory"])
app.include_router(sales.router, prefix="/api/v1/sales", tags=["sales"])
app.include_router(customers.router, prefix="/api/v1/customers", tags=["customers"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])

@app.get("/")
async def root():
    return {"message": "Welcome to Sell Sync POS API"}
