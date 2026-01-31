from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sell Sync"
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "sell_sync"
    secret_key: str = "YOUR_SECRET_KEY"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
