from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.expenses import Expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse

router = APIRouter()

# GET all Expenses
@router.get("/", response_model=List[ExpenseResponse])
async def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return expenses

# GET a single expense by ID
@router.get("/{expense_id}", response_model=ExpenseResponse)
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="expense not found"
        )
    return expense

# POST create a new expense
@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
async def create_expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
    # Check if expense already exists
    existing_expense = db.query(Expense).filter(Expense.description == expense_data.description).first()
    if existing_expense:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Expense with this description already exists"
        )

    # Create new expense
    expense = Expense(
        company_id=expense_data.company_id,
        category_id=expense_data.category_id,
        account_id=expense_data.account_id,
        amount=expense_data.amount,
        description=expense_data.description
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense

# PUT update an expense
@router.put("/{expense_id}", response_model=ExpenseResponse)
async def update_expense(
    expense_id: int,
    expense_data: ExpenseCreate,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )
    
    # Update expense using setattr for better maintainability
    setattr(expense, "company_id", expense_data.company_id)
    setattr(expense, "category_id", expense_data.category_id)
    setattr(expense, "account_id", expense_data.account_id)
    setattr(expense, "amount", expense_data.amount)
    setattr(expense, "description", expense_data.description)
    db.commit()
    db.refresh(expense)
    
    return expense

# DELETE an expense
@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )
    
    db.delete(expense)
    db.commit()
    
    return None