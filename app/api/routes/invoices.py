from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceResponse

router = APIRouter()

# GET all invoices
@router.get("/", response_model=List[InvoiceResponse])
async def get_invoices(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()
    return invoices

# GET a single invoice by ID
@router.get("/{invoice_id}", response_model=InvoiceResponse)
async def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )
    return invoice

# POST create a new invoice
@router.post("/", response_model=InvoiceResponse, status_code=status.HTTP_201_CREATED)
async def create_invoice(invoice_data: InvoiceCreate, db: Session = Depends(get_db)):
    
    # Create new invoice
    invoice = Invoice(
        company_id=invoice_data.company_id,
        invoice_number=invoice_data.invoice_number,
        amount=invoice_data.amount,
        due_date=invoice_data.due_date,
        issue_date=invoice_data.issue_date, 
        status=invoice_data.status
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice

# PUT update a invoice
@router.put("/{invoice_id}", response_model=InvoiceResponse)
async def update_invoice(
    invoice_id: int,
    invoice_data: InvoiceCreate,
    db: Session = Depends(get_db)
):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    # Update invoice using setattr for better maintainability
    setattr(invoice, "company_id", invoice_data.company_id)
    setattr(invoice, "invoice_number", invoice_data.invoice_number)
    setattr(invoice, "amount", invoice_data.amount)
    setattr(invoice, "due_date", invoice_data.due_date)
    setattr(invoice, "issue_date", invoice_data.issue_date)
    setattr(invoice, "status", invoice_data.status)
    db.commit()
    db.refresh(invoice)

    return invoice

# DELETE a invoice
@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    db.delete(invoice)
    db.commit()
    
    return None