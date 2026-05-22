from pydantic_settings import BaseSettings
from typing import Optional
class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str="sqlite:///./accounting.db"
    
    # JWT Security settings
    SECRET_KEY: str="your-secret-key-here-change-this-in-production"
    ALGORITHM: str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int=30
    
    #CORS settings
    cors_origins: Optional[list[str]] = ["http://localhost:3000", "http://localhost:5173"]
    
    class Config:
        env_file = ".env"
        
settings = Settings()
