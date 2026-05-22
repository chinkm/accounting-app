from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InvoiceBase(BaseModel):
    company_id: int
    invoice_number: str
    amount: float    
    due_date: Optional[datetime]  = None  
    issue_date: Optional[datetime] = None  
    status: Optional[str]  = "pending"  # "pending", "paid", "overdue"             
    


class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {
        "from_attributes": True}