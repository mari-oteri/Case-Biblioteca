from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers import user_router, author_router, book_router, loan_router
from app.db.database import SessionLocal
from app.core.data import seed_data

app = FastAPI(title="Digital Library API")

Base.metadata.create_all(bind=engine)

db = SessionLocal()
seed_data(db)
db.close()

app.include_router(user_router.router)
app.include_router(author_router.router)
app.include_router(book_router.router)
app.include_router(loan_router.router)


@app.get("/")
def health():
    return {"status": "ok"}


