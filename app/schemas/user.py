from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    name: str
    role: Optional[str] = None  # Optional role field for user roles (e.g., admin, user)
    company_id: int


class UserCreate(UserBase):
    password: str  # Password is required for creating a user


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
