from sqlalchemy.orm import Session
from app.repositories import  book_repository

def list_books(db: Session, page: int, size: int):
    return book_repository.get_all_books(db, page, size)