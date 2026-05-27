from app.api.routes.users import router as users_router
from app.api.routes.companies import router as companies_router
from app.api.routes.categories import router as categories_router
from app.api.routes.accounts import router as accounts_router
from app.api.routes.invoices import router as invoices_router
from app.api.routes.expenses import router as expenses_router
from app.api.routes.income import router as income_router
from app.api.routes.transactions import router as transactions_router

from fastapi import APIRouter

# Create routers
users_router = APIRouter()
companies_router = APIRouter()
categories_router = APIRouter()
accounts_router = APIRouter()
invoices_router = APIRouter()
expenses_router = APIRouter()
income_router = APIRouter()
transactions_router = APIRouter()
auth_router = APIRouter() # Add auth router

__all__ = [
    "users_router",
    "companies_router",
    "categories_router",
    "accounts_router",
    "invoices_router",
    "expenses_router",
    "income_router",
    "transactions_router",
    "auth_router", # Include auth router in __all__
]