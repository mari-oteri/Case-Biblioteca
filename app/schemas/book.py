from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author_id: int
    total_copies: int

class BookResponse(BaseModel):
    id: int
    title: str
    author_id: int
    total_copies: int
    available_copies: int

    class Config:
        from_attributes = True
