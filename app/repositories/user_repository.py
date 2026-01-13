from sqlalchemy.orm import Session
from app.db import models
from app.core.pagination import paginate

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session, page: int, size: int):
    query = db.query(models.User)
    return paginate(query, page, size).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

