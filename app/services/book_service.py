from sqlalchemy.orm import Session
from app.repositories.book_repository import create_book_repo, get_book_by_id, get_all_books

def list_books(db: Session, page: int, size: int):
    return get_all_books(db, page, size)


def create_book(db: Session, title: str, author_id: int, total_copies: int):
    return create_book_repo(db, title, author_id, total_copies)


def get_book(db: Session, book_id: int):
    return get_book_by_id(db, book_id)