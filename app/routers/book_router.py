from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookResponse
from app.services import book_service
from app.db.database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book.title, book.author_id, book.total_copies)

@router.get("/", response_model=list[BookResponse])
def list_books(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    return book_service.list_books(db, page, size)

@router.get("/{book_id}/available")
def check_availability(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"available_copies": book.available_copies}
