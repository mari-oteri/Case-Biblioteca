from sqlalchemy.orm import Session
from app.db import models
from app.core.pagination import paginate

def create_loan(db: Session, loan: models.Loan):
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

def get_active_loans_by_user(db: Session, user_id: int):
    return db.query(models.Loan).filter(
        models.Loan.user_id == user_id,
        models.Loan.return_date is None
    ).all()

def get_loan_by_id(db: Session, loan_id: int):
    return db.query(models.Loan).filter(models.Loan.id == loan_id).first()

def list_active_loans(db: Session, page: int, size: int):
    query = db.query(models.Loan).filter(models.Loan.return_date is None)
    return paginate(query, page, size).all()

def list_overdue_loans(db: Session, today):
    return db.query(models.Loan).filter(
        models.Loan.return_date is None,
        models.Loan.due_date < today
    ).all()

def get_loans_by_user(db: Session, user_id: int):
    return db.query(models.Loan).filter(models.Loan.user_id == user_id).all()