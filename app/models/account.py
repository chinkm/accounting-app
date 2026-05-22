from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.models import Base
from datetime import datetime

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # "bank", "cash", "credit_card", etc.
    balance = Column(Numeric(10, 2), default=0.00)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Relationships
    transactions = relationship("Transaction", back_populates="account")
    income = relationship("Income", back_populates="account")
    expenses = relationship("Expense", back_populates="account")
    company = relationship("Company", back_populates="accounts")
    