from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class IncomeBase(BaseModel):
    company_id: int
    category_id: int
    account_id: int
    amount: float
    description: str
    date: Optional[datetime] = None
    invoice_id: Optional[int] = None
    reference_number: Optional[str] = None
    payment_method: Optional[str] = None
    status: str = "pending"
    tax_amount: float = 0.00
    tax_rate: float = 0.00
    notes: Optional[str] = None

class IncomeCreate(IncomeBase):
    pass

class IncomeUpdate(BaseModel):
    company_id: Optional[int] = None
    category_id: Optional[int] = None
    account_id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    invoice_id: Optional[int] = None
    reference_number: Optional[str] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None
    tax_amount: Optional[float] = None
    tax_rate: Optional[float] = None
    notes: Optional[str] = None

class IncomeResponse(IncomeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}