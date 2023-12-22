from typing import List
from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    author_id: int
    title: str
    genre: str
    publication_year: datetime
    code: int
    availability_status: bool

class BookResponse(BaseModel):
    book_id: int
    author_id: int
    title: str
    genre: str
    publication_year: datetime
    code: int
    availability_status: bool


class AuthorCreate(BaseModel):
    full_name: str
    birth_year: datetime
    country: str

class AuthorResponse(BaseModel):
    author_id: int
    full_name: str
    birth_year: datetime
    country: str
    books: List[BookResponse]


class GenreCreate(BaseModel):
    genre_name: str

class GenreResponse(BaseModel):
    genre_id: int
    genre_name: str
