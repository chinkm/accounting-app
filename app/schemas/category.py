from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

from app.schemas.user import UserBase

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str  # "expense" or "income"

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {
        "from_attributes": True}