from sqlalchemy.orm import Session
from app.db import models

def create_author(db: Session, name: str):
    author = models.Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_all_authors(db: Session):
    return db.query(models.Author).all()
