# create_seed_data.py
from app.database import SessionLocal
from app.models.companies import Company  # ✅ Import directly
from app.models.account import Account
from app.models.category import Category
from app.models.income import Income
from app.models.expenses import Expense
from app.models.transaction import Transaction
from app.models.invoice import Invoice

def create_seed_data():
    db = SessionLocal()
    
    # Create a company
    company = Company(
        name="CKM Company",
        email="ckmo@mycompany.com",
        phone="+60128666789",
        address="123 Main Street, Sandakan, Sabah"
    )
    db.add(company)
    db.commit()
    db.refresh(company)
    
    # Create accounts
    bank_account = Account(
        company_id=company.id,
        name="Bank Account",
        type="bank",
        balance=5000.00,
        description="Main bank account"
    )
    db.add(bank_account)
    
    cash_account = Account(
        company_id=company.id,
        name="Cash",
        type="cash",
        balance=1500.00,
        description="Cash on hand"
    )
    db.add(cash_account)
    
    # Create categories
    income_category = Category(
        #company_id=company.id,
        name="Sales",
        type="income",
        description="Sales income"
    )
    db.add(income_category)
    
    expense_category = Category(
        #company_id=company.id,
        name="Water",
        type="expense",
        description="Water bill expenses"
    )
    db.add(expense_category)
    
    db.commit()
    db.refresh(company)
    db.refresh(bank_account)
    db.refresh(cash_account)
    db.refresh(income_category)
    db.refresh(expense_category)
    
    print("✅ Seed data created successfully!")
    print(f"Company ID: {company.id}")
    print(f"Bank Account ID: {bank_account.id}")
    print(f"Cash Account ID: {cash_account.id}")
    print(f"Income Category ID: {income_category.id}")
    print(f"Expense Category ID: {expense_category.id}")
    
    db.close()

if __name__ == "__main__":
    create_seed_data()