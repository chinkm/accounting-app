from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    account_id: int
    amount: float
    type: str  # "expense" or "income"
    description: str
    date: Optional[datetime] = None
    reference_number: Optional[str] = None
    payment_method: Optional[str] = None
    status: str = "completed"
    category_id: Optional[int] = None
    notes: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    account_id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    reference_number: Optional[str] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None
    category_id: Optional[int] = None
    notes: Optional[str] = None

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}