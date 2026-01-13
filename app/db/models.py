from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import date

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(Date, default=date.today)

    loans = relationship("Loan", back_populates="user")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    total_copies = Column(Integer, default=1)
    available_copies = Column(Integer, default=1)

    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    loan_date = Column(Date, default=date.today)
    due_date = Column(Date)
    return_date = Column(Date, nullable=True)
    fine_amount = Column(Integer, default=0)

    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
