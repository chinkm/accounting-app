from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from decimal import Decimal


class AccountBase(BaseModel):
    type: str  # "bank", "cash", "credit_card", etc.
    name: str
    balance: Optional[Decimal] = Decimal("0.00")
    description: Optional[str] = None


class AccountCreate(AccountBase):
    pass


class AccountResponse(AccountBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    company_id: int  # Foreign key to the company that owns this account

    model_config = {"from_attributes": True}
