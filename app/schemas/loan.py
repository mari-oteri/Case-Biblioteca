from pydantic import BaseModel
from datetime import date

class LoanCreate(BaseModel):
    user_id: int
    book_id: int

class LoanResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    loan_date: date
    due_date: date
    return_date: date | None
    fine_amount: int

    class Config:
        from_attributes = True
