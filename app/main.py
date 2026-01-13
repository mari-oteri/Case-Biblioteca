from fastapi import FastAPI

from app.db.database import Base, engine
from app.db import models

from app.routers import user_router, author_router, book_router, loan_router

app = FastAPI(title="Digital Library API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(author_router.router)
app.include_router(book_router.router)
app.include_router(loan_router.router)


@app.get("/")
def health():
    return {"status": "ok"}


