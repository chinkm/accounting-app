from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.models import Base
from datetime import datetime

class Income(Base):
    __tablename__ = "income"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    
    # Core fields
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    # Optional fields
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=True)
    reference_number = Column(String, nullable=True)  # For bank statements, etc.
    payment_method = Column(String, nullable=True)  # "bank_transfer", "cash", "credit_card", etc.
    status = Column(String, default="pending")  # "pending", "received", "partial", "overdue"
    
    # Tax fields
    tax_amount = Column(Numeric(10, 2), default=0.00)
    tax_rate = Column(Numeric(5, 2), default=0.00)  # Percentage
    
    # Additional fields
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    company = relationship("Company", back_populates="income")
    category = relationship("Category", back_populates="income")
    account = relationship("Account", back_populates="income")
    invoice = relationship("Invoice", back_populates="income")