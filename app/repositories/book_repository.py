from sqlalchemy.orm import Session
from app.db import models

def create_book(db: Session, title: str, author_id: int, total: int):
    book = models.Book(
        title=title,
        author_id=author_id,
        total_copies=total,
        available_copies=total
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_all_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()
