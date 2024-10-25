# Step 1: Installation of Required Libraries
# pip install fastapi
# pip install pydantic
# pip install sqlalchemy
# pip install uvicorn

# Referance => https://www.geeksforgeeks.org/fastapi-sqlite-databases/

# Step 2: Importing Necessary Libraries and Classes
from fastapi import FastAPI, HTTPException, Depends
import uvicorn

# Import necessary modules and classes
from pydantic import BaseModel, Field
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

# Step 5: Creating Database Tables
# Let's create a necessary tables in the database based on the defined models.
models.Base.metadata.create_all(bind=engine)

# Step 6: Dependency for Getting the Database Session
# In this step We will define a dependency function (get_db) to get a database session. It yields the database session to be used in API endpoints and ensures that the database session is properly closed after use by API.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Step 7: Pydantic model for request data
class BookRequestModel(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    author : str = Field(min_length=1, max_length=100)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, le=5) # gt : gether then, le : less then or equal
    
# Step 7: Pydantic model for response data
class BookResponseModel(BaseModel):
    id : int
    title : str
    author : str
    description : str
    rating : int
    


# >>>>>>>>>>>>>>>>>>>>> Routes or API code <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@app.get('/', tags=['Home Page'])
async def Home():
    return {'message' : 'This is Home Page'}


# >>>>>>>>> Get All Books -----------
@app.get('/books/', response_model=List[BookResponseModel], tags=["Books"])
async def find_all_book(db : Session = Depends(get_db)):
    books = db.query(models.BooksModel).all()
    return books

# >>>>>>>> Get a Specific Book ---------
@app.get('/book/{book_id}', response_model=BookResponseModel, tags=["Books"])
async def find_single_book(book_id : int, db : Session=Depends(get_db)):
    book = db.query(models.BooksModel).filter(models.BooksModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book Not Found")
    return book


# >>>>>>>>> Create a New Book --------
@app.post('/book/', response_model=BookResponseModel, tags=['Books'])
async def create_new_book(book : BookRequestModel, db : Session = Depends(get_db)):
    book_model = models.BooksModel(**book.dict())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    return book_model

# >>>>>>>>> Update a Book -------------
@app.put('/book/{book_id}', response_model=BookResponseModel, tags=["Books"])
async def update_book(book_id : int, book_request : BookRequestModel,db : Session = Depends(get_db)):
    book_model = db.query(models.BooksModel).filter(models.BooksModel.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book Not Found")
    book_model.title = book_request.title
    book_model.author = book_request.author
    book_model.description = book_request.description
    book_model.rating = book_request.rating
    
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    return book_model
    
    
# >>>>>>>> Delete a Book ----------
@app.delete('/book/{book_id}', tags=['Books'])
async def delete_book(book_id : int, db : Session = Depends(get_db)):
    book_model = db.query(models.BooksModel).filter(models.BooksModel.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    db.query(models.BooksModel).filter(models.BooksModel.id == book_id).delete()
    db.commit()
    return {"message" : f"Book (book_id={book_id}) Delete Successfully."}
    
    
    
# Step 10: Running the FastAPI Application
if __name__ == '__main__':
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
