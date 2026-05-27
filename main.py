from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from app.api.routes.auth import router as auth_router
from app.api.routes import (
    users_router,
    companies_router,
    categories_router,
    accounts_router,
    invoices_router,
    expenses_router,
    income_router,
    transactions_router,
)

# Create FastAPI app
app = FastAPI(
    title="Accounting API",
    description="API for managing companies, invoices, expenses, and income",
    version="1.0.0",
)

# Creaate all tables in the database (for development purposes)
from app.database import engine
from app.models import Base 
Base.metadata.create_all(bind=engine)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(companies_router, prefix="/api/companies", tags=["Companies"])
app.include_router(categories_router, prefix="/api/categories", tags=["Categories"])
app.include_router(accounts_router, prefix="/api/accounts", tags=["Accounts"])
app.include_router(invoices_router, prefix="/api/invoices", tags=["Invoices"])
app.include_router(expenses_router, prefix="/api/expenses", tags=["Expenses"])
app.include_router(income_router, prefix="/api/income", tags=["Income"])
app.include_router(transactions_router, prefix="/api/transactions", tags=["Transactions"])
app.include_router(auth_router, prefix="/api", tags=["Authentication"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Accounting API",
        "version": "1.0.0",
        "docs": "/docs",
    }
#Print the Real Routes to Debug    
@app.on_event("startup")
def print_routes():
    for route in app.routes:
        if isinstance(route, APIRoute):
            print(f"Route Name: {route.name}, Path: {route.path}")