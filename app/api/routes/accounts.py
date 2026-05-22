from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountResponse

router = APIRouter()

# GET all accounts
@router.get("/", response_model=List[AccountResponse])
async def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return accounts

# GET a single account by ID
@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    return account

# POST create a new account
@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(account_data: AccountCreate, db: Session = Depends(get_db)):
    # Check if account already exists
    existing_account = db.query(Account).filter(Account.name == account_data.name).first()
    if existing_account:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account with this name already exists"
        )
    
    # Create new account
    account = Account(
        name=account_data.name,
        type=account_data.type,
        description=account_data.description,
        balance=account_data.balance
    )
    db.add(account)
    db.commit()
    db.refresh(account)

    return account

# PUT update a account
@router.put("/{account_id}", response_model=AccountResponse)
async def update_account(
    account_id: int,
    account_data: AccountCreate,
    db: Session = Depends(get_db)
):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )

    # Update account using setattr for better maintainability
    setattr(account, "name", account_data.name)
    setattr(account, "type", account_data.type)
    setattr(account, "description", account_data.description)
    setattr(account, "balance", account_data.balance)
    db.commit()
    db.refresh(account)

    return account

# DELETE a account
@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )

    db.delete(account)
    db.commit()
    
    return None