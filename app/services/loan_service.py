from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.db import models
from app.repositories import loan_repository, book_repository

MAX_LOANS = 3
LOAN_DAYS = 14
FINE_PER_DAY = 2

def create_loan(db: Session, user_id: int, book_id: int):
    active_loans = loan_repository.get_active_loans_by_user(db, user_id)
    if len(active_loans) >= MAX_LOANS:
        raise Exception("User reached maximum number of active loans")

    book = book_repository.get_book_by_id(db, book_id)
    if book.available_copies < 1:
        raise Exception("Book not available")

    book.available_copies -= 1

    today = date.today()
    due_date = today + timedelta(days=LOAN_DAYS)

    loan = models.Loan(
        user_id=user_id,
        book_id=book_id,
        loan_date=today,
        due_date=due_date
    )

    return loan_repository.create_loan(db, loan)

def return_loan(db: Session, loan_id: int):
    loan = loan_repository.get_loan_by_id(db, loan_id)
    if not loan or loan.return_date:
        raise Exception("Invalid loan")

    today = date.today()
    loan.return_date = today

    days_late = (today - loan.due_date).days
    loan.fine_amount = max(0, days_late * FINE_PER_DAY)

    loan.book.available_copies += 1

    db.commit()
    return loan

def list_active_loans(db: Session):
    return loan_repository.list_active_loans(db)

def list_overdue_loans(db: Session):
    return loan_repository.list_overdue_loans(db, date.today())
