from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from fastapi import APIRouter

book_router = APIRouter(
    prefix="/books",
    tags=["books"]
)

books = [
{
"id":"1239",
"title": "Python Basics",
"author": "John Smith",
"category": "programming"
},
{
"id":"1232",

"title": "Machine Learning",
"author": "Sarah Johnson",
"category": "science"
},
{
"id":"12139",

"title": "World History",
"author": "David Brown",
"category": "history"
},
{
"id":"129039",

"title": "Advanced Mathematics",
"author": "Emily White",
"category": "math"
},
{
"id":"1289039",

"title": "Physics Fundamentals",
"author": "Michael Green",
"category": "science"
},
{
"id":"1291139",

"title": "JavaScript Guide",
"author": "Alex Wilson",
"category": "programming"
}
]

class Book(BaseModel):
    id: str
    title:str = None
    author:str
    category:str

@book_router.delete("/books_delete", status_code=201)
def delete_book(id: str):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return book
    return {"id": "No book found"}            


@book_router.post("/create_book", status_code=201)
def create_book(new_book:Book):
    books.append(new_book)
    # return {"new_book": books[new_book["id"]]}
    return {"new_book": new_book}

@book_router.get("")
def get_books(category:str|None=Query(
    min_length = 6, 
    max_length= 10
) ):
    category_book = []
    if category == None:
        return books
    # for book in books:
    #     if book["category"].lower() == category.lower():
    #         category_book.append(book)
    # return category_book

    return [
        book for book in books 
        if book["category"] == category
    ]
    

@book_router.get("/{id}")
def get_book(id:str):
    # for book in books:
    #     if book["id"] == id:
    #         return book
    # return {"id": "No record found"}

    return next((book for book in books if book["id"]==id), 
                ({"id": "No record found"}))

# return next((first), (or second))


@book_router.put("/update")
def update_book(newbook:Book):
    for book in books:
        if book["id"] == newbook.id:
            book["title"] = newbook.title
            book["author"] = newbook.author
            book["category"] = newbook.category
            return book

class UPDATED_BOOK(BaseModel):
    # title:str|None=None
    title:str|None = Field(default=None, min_length=6, max_length=30)
    author:str|None=None
    category:str|None=None

@book_router.patch("/updatebooks/{id}")
def update_book(id, newbook:UPDATED_BOOK):
    update_book = newbook.model_dump(exclude_unset=True)
    
    for book in books:
        if book["id"] == id:
            book.update(update_book)
            return {"book": book}
    return HTTPException(status_code=404, detail="ID NOT FOUND, its wrong ID")