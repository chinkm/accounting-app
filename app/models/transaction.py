from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.models import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    
    # Core fields
    amount = Column(Numeric(10, 2), nullable=False)
    type = Column(String, nullable=False)  # "expense" or "income"
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    # Optional fields
    reference_number = Column(String, nullable=True)  # For bank statements, etc.
    payment_method = Column(String, nullable=True)  # "bank_transfer", "cash", "credit_card", etc.
    status = Column(String, default="completed")  # "pending", "completed", "cancelled"
    
    # Category field (optional - for better organization)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Additional fields
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    
    company = relationship("Company", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
    account=relationship("Account", back_populates="transactions")