from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.models import Base
from datetime import datetime

class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    invoice_number = Column(String, nullable=False, unique=True)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String, default="pending")  # "pending", "paid", "overdue"
    due_date = Column(DateTime)
    issue_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    company = relationship("Company", back_populates="invoices")
    # items = relationship("InvoiceItem", back_populates="invoice")
    income = relationship("Income", back_populates="invoice")