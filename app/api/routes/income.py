from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.income import Income
from app.schemas.income import IncomeCreate, IncomeUpdate, IncomeResponse

router = APIRouter()

# GET all income
@router.get("/", response_model=List[IncomeResponse])
async def get_income(db: Session = Depends(get_db)):
    income_list = db.query(Income).all()
    return income_list

# GET a single income by ID
@router.get("/{income_id}", response_model=IncomeResponse)
async def get_income_item(income_id: int, db: Session = Depends(get_db)):
    income_item = db.query(Income).filter(Income.id == income_id).first()
    if not income_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    return income_item

# POST create a new income
@router.post("/", response_model=IncomeResponse, status_code=status.HTTP_201_CREATED)
async def create_income(income_data: IncomeCreate, db: Session = Depends(get_db)):
    # Create new income
    income = Income(
        company_id=income_data.company_id,
        category_id=income_data.category_id,
        account_id=income_data.account_id,
        amount=income_data.amount,
        description=income_data.description,
        date=income_data.date,
        invoice_id=income_data.invoice_id,
        reference_number=income_data.reference_number,
        payment_method=income_data.payment_method,
        status=income_data.status,
        tax_amount=income_data.tax_amount,
        tax_rate=income_data.tax_rate,
        notes=income_data.notes,
    )
    db.add(income)
    db.commit()
    db.refresh(income)
    
    return income

# PUT update an income
@router.put("/{income_id}", response_model=IncomeResponse)
async def update_income(
    income_id: int,
    income_data: IncomeUpdate,
    db: Session = Depends(get_db)
):
    income = db.query(Income).filter(Income.id == income_id).first()
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    # Update income using setattr
    if income_data.company_id is not None:
        setattr(income, 'company_id', income_data.company_id)
    if income_data.category_id is not None:
        setattr(income, 'category_id', income_data.category_id)
    if income_data.account_id is not None:
        setattr(income, 'account_id', income_data.account_id)
    if income_data.amount is not None:
        setattr(income, 'amount', income_data.amount)
    if income_data.description is not None:
        setattr(income, 'description', income_data.description)
    if income_data.date is not None:
        setattr(income, 'date', income_data.date)
    if income_data.invoice_id is not None:
        setattr(income, 'invoice_id', income_data.invoice_id)
    if income_data.reference_number is not None:
        setattr(income, 'reference_number', income_data.reference_number)
    if income_data.payment_method is not None:
        setattr(income, 'payment_method', income_data.payment_method)
    if income_data.status is not None:
        setattr(income, 'status', income_data.status)
    if income_data.tax_amount is not None:
        setattr(income, 'tax_amount', income_data.tax_amount)
    if income_data.tax_rate is not None:
        setattr(income, 'tax_rate', income_data.tax_rate)
    if income_data.notes is not None:
        setattr(income, 'notes', income_data.notes)
    
    db.commit()
    db.refresh(income)
    
    return income

# DELETE an income
@router.delete("/{income_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_income(income_id: int, db: Session = Depends(get_db)):
    income = db.query(Income).filter(Income.id == income_id).first()
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    db.delete(income)
    db.commit()
    return None 