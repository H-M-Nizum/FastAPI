# Step 4: Defining the Database Model
# In this step we will create a database model named Item(using sqlalchemy Base model) in our database, we store all our data into this model. 
# The model named Item represents items with an id, name, and description. here id, name and description are data field of model.
from sqlalchemy import Column, Integer, String
from db import Base # from db.py

class BooksModel(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
    
