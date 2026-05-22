from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import user
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate, TransactionResponse, TransactionUpdate



router = APIRouter()

# GET all users
@router.get("/", response_model=List[TransactionResponse])
async def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

# GET a single transaction by ID
@router.get("/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return transaction

# POST create a new transaction
@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    # Check if transaction already exists
    existing_transaction = db.query(Transaction).filter(Transaction.description == transaction_data.description).first()
    if existing_transaction:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transaction with this description already exists"
        )

    # Create new transaction
    transaction = Transaction(
        account_id=transaction_data.account_id,
        amount=transaction_data.amount,
        type=transaction_data.type,
        description=transaction_data.description,
        date=transaction_data.date,
        reference_number=transaction_data.reference_number,
        payment_method=transaction_data.payment_method,
        status=transaction_data.status,
        category_id=transaction_data.category_id,
        notes=transaction_data.notes
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

# PUT update a transaction
@router.put("/{transaction_id}", response_model=TransactionResponse)
async def update_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    # Update transaction using setattr for better maintainability
    setattr(transaction, "account_id", transaction_data.account_id)
    setattr(transaction, "amount", transaction_data.amount)
    setattr(transaction, "type", transaction_data.type)
    setattr(transaction, "description", transaction_data.description)
    setattr(transaction, "date", transaction_data.date)
    setattr(transaction, "reference_number", transaction_data.reference_number)
    setattr(transaction, "payment_method", transaction_data.payment_method)
    setattr(transaction, "status", transaction_data.status)
    setattr(transaction, "category_id", transaction_data.category_id)
    setattr(transaction, "notes", transaction_data.notes)
    db.commit()
    db.refresh(transaction)

    return transaction

# DELETE a transaction
@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    db.delete(transaction)
    db.commit()
    
    return None