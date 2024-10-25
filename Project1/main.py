# FastAPI is a Python class that provides all the functionality for your API.
from fastapi import FastAPI, HTTPException

# Here the app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.
app = FastAPI()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Simple Get API >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A path operation decorator using decorators like @app.get("/").
# the path /
# using a get operation
@app.get('/')
# This is a path operation Python function. It receives a request to the URL "/" using a GET operation.
# In this case, it is an async function.
async def home():
    # You can return a dict, list, singular values as str, int, etc.
    # You can also return Pydantic models (you'll see more about that later).
    return {'message' : 'This is FastAPI home page.'}


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Function Receive a Parameters From URL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.get('/receive_parameter/{name}')
async def receive_parameter(name : str):
    return {'message' : f'My name is {name}'}

# parameter not require
@app.get('/receive_optional_parameter/')
async def receive_optional_parameter(name: str = None):
    return {'message': f'My name is {name if name else "not provided"}'}


# >>>>>>>>>>>>>>>>>>>>>>>>>>>> Using Pyddantic for ORM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# models.py file
from pydantic import BaseModel, Field
from uuid import UUID

class BookModel(BaseModel):
    id : UUID
    title : str = Field(min_length=1, max_length=100)
    author : str = Field(min_length=1, max_length=100)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, le=5) # gt : gether then, le : less then or equal
    
Books = []

# Create a new book
@app.post('/create_book/', tags=['Using Pydantic for ORM'])
async def create_new_book(book : BookModel):
    Books.append(book)
    return {'message' : 'Successfully Create a New Book', 'data' : book}

# Get all books
@app.get('/books/', tags=['Using Pydantic for ORM'])
async def find_all_book():
    return {'message' : 'All The Book', 'data' : Books}

# Get a specific book using by id
@app.get('/books/{id}', tags=['Using Pydantic for ORM'])
async def find_specific_book(id : UUID):
    for i in Books:
        if i.id == id:
            return {'message' : 'All The Book', 'data' : i}
    raise HTTPException(status_code=404, detail="Book are not found")

# Update a specific Book
@app.put('/book/{id}', tags=['Using Pydantic for ORM'])
async def update_specific_book(id : UUID, book : BookModel):
    count = 0
    for i in Books:
        if i.id == id:
            Books[count] = book
            return {"message":"Book Update Successfully", "data":book}
        count += 1
    raise HTTPException(status_code=404, detail="Book are not found")

# Delete a specific Book
@app.delete('/book/{id}', tags=['Using Pydantic for ORM'])
async def delete_specific_book(id : UUID):
    count = 0
    for i in Books:
        if i.id == id:
            book = Books[count]
            del Books[count]
            return {"message":"Book Delete Successfully", "data":book}
        count += 1
    raise HTTPException(status_code=404, detail="Book are not found")