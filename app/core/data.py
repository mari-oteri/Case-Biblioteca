
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.db import models

def seed_data(db: Session):
    if db.query(models.User).first():
        return  

    users = [
        models.User(name="Alice", email="alice@email.com"),
        models.User(name="Bruno", email="bruno@email.com"),
        models.User(name="Carla", email="carla@email.com"),
    ]
    db.add_all(users)

    authors = [
        models.Author(name="George Orwell"),
        models.Author(name="J.K. Rowling"),
        models.Author(name="Machado de Assis"),
    ]
    db.add_all(authors)
    db.commit()

    books = [
        models.Book(title="1984", author_id=authors[0].id, total_copies=3, available_copies=3),
        models.Book(title="Harry Potter", author_id=authors[1].id, total_copies=5, available_copies=5),
        models.Book(title="Dom Casmurro", author_id=authors[2].id, total_copies=2, available_copies=2),
    ]
    db.add_all(books)
    db.commit()

    loan = models.Loan(
        user_id=users[0].id,
        book_id=books[0].id,
        loan_date=date.today() - timedelta(days=10),
        due_date=date.today() + timedelta(days=4),
    )
    books[0].available_copies -= 1

    db.add(loan)
    db.commit()