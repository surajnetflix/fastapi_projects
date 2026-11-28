from fastapi import FastAPI
from routers import books

app = FastAPI()

app.include_router(books.book_router)

@app.get("/")
def welcome():
    return {"Hello": "World"}


