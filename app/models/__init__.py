from sqlalchemy.orm import DeclarativeBase


# Create a base class for our models
class Base(DeclarativeBase):
    pass


# import all models to ensure they are registered with SQLAlchemy
from app.models.companies import Company
from app.models.invoice import Invoice
from app.models.expenses import Expense
from app.models.account import Account
from app.models.income import Income
from app.models.transaction import Transaction
from app.models.user import User
from app.models.category import Category

# Expose the models for easy access
__all__ = [
    "Base",
    "Company",
    "Invoice",
    "Expense",
    "Account",
    "Income",
    "Transaction",
    "User",
    "Category",
]
