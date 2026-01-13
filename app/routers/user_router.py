from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.schemas.loan import LoanResponse
from app.services import user_service, loan_service
from app.db.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user.name, user.email)

@router.get("/", response_model=list[UserResponse])
def list_users(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    return user_service.list_users(db, page, size)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/loans", response_model=list[LoanResponse])
def user_loans(user_id: int, db: Session = Depends(get_db)):
    return loan_service.get_user_loans(db, user_id)