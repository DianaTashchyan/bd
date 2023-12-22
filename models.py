from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'), nullable=False)
    title = Column(String(255))
    genre = Column(String(50))
    publication_year = Column(Date)
    code = Column(Integer)
    availability_status = Column(Boolean)

    author = relationship("Author", back_populates="books")

class Author(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(255))
    birth_year = Column(Date)
    country = Column(String(50))

    books = relationship("Book", back_populates="author")

class Genre(Base):
    __tablename__ = "genres"

    genre_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    genre_name = Column(String(50))
