from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_book, read_all_books, read_book, update_book, delete_book
from crud import create_author, read_all_authors, read_author, update_author, delete_author
from crud import create_genre, read_all_genres, read_genre, update_genre, delete_genre
from db_dependencies import get_db
from schemas import *

book_router = APIRouter()


@book_router.post("/books/", response_model=BookResponse)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)

@book_router.get("/books/{book_id}", response_model=BookResponse)
def read_book_route(book_id: int, db: Session = Depends(get_db)):
    return read_book(db=db, book_id=book_id)

@book_router.get("/books/", response_model=List[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    return read_all_books(db=db)

@book_router.put("/books/{book_id}", response_model=BookResponse)
def update_book_route(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    return update_book(db=db, book_id=book_id, updated_book=updated_book)

@book_router.delete("/books/{book_id}", response_model=BookResponse)
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    return delete_book(db=db, book_id=book_id)


author_router = APIRouter()


@author_router.post("/authors/", response_model=AuthorResponse)
def create_author_route(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db=db, author=author)

@author_router.get("/authors/{author_id}", response_model=AuthorResponse)
def read_author_route(author_id: int, db: Session = Depends(get_db)):
    return read_author(db=db, author_id=author_id)

@author_router.get("/authors/", response_model=List[AuthorResponse])
def get_all_authors(db: Session = Depends(get_db)):
    return read_all_authors(db=db)

@author_router.put("/authors/{author_id}", response_model=AuthorResponse)
def update_author_route(author_id: int, updated_author: AuthorCreate, db: Session = Depends(get_db)):
    return update_author(db=db, author_id=author_id, updated_author=updated_author)

@author_router.delete("/authors/{author_id}", response_model=AuthorResponse)
def delete_author_route(author_id: int, db: Session = Depends(get_db)):
    return delete_author(db=db, author_id=author_id)


genre_router = APIRouter()


@genre_router.post("/genres/", response_model=GenreResponse)
def create_genre_route(genre: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db=db, genre=genre)

@genre_router.get("/genres/{genre_id}", response_model=GenreResponse)
def read_genre_route(genre_id: int, db: Session = Depends(get_db)):
    return read_genre(db=db, genre_id=genre_id)

@genre_router.get("/genres/", response_model=List[GenreResponse])
def get_all_genres(db: Session = Depends(get_db)):
    return read_all_genres(db=db)

@genre_router.put("/genres/{genre_id}", response_model=GenreResponse)
def update_genre_route(genre_id: int, updated_genre: GenreCreate, db: Session = Depends(get_db)):
    return update_genre(db=db, genre_id=genre_id, updated_genre=updated_genre)

@genre_router.delete("/genres/{genre_id}", response_model=GenreResponse)
def delete_genre_route(genre_id: int, db: Session = Depends(get_db)):
    return delete_genre(db=db, genre_id=genre_id)
