from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
next_book_id = 3
