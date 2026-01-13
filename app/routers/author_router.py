from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.author import AuthorCreate, AuthorResponse
from app.services import author_service
from app.db.database import SessionLocal

router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(db, author.name)

@router.get("/", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return author_service.list_authors(db)
