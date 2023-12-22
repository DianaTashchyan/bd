from fastapi import FastAPI
from routes import book_router, author_router, genre_router

app = FastAPI()

app.include_router(book_router, tags=["books"])
app.include_router(author_router, tags=["authors"])
app.include_router(genre_router, tags=["genres"])