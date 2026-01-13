from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.loan import LoanCreate, LoanResponse
from app.services import loan_service
from app.db.database import SessionLocal

router = APIRouter(prefix="/loans", tags=["Loans"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LoanResponse)
def create_loan(data: LoanCreate, db: Session = Depends(get_db)):
    try:
        return loan_service.create_loan(db, data.user_id, data.book_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{loan_id}/return", response_model=LoanResponse)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    try:
        return loan_service.return_loan(db, loan_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/active", response_model=list[LoanResponse])
def active_loans(db: Session = Depends(get_db)):
    return loan_service.list_active_loans(db)

@router.get("/overdue", response_model=list[LoanResponse])
def overdue_loans(db: Session = Depends(get_db)):
    return loan_service.list_overdue_loans(db)
