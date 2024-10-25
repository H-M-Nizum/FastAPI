from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Step 3: Creating a FastAPI Instance and SetUp the Database
#  Set up the database connection using SQLite and create a SQLAlchemy engine also Defined a SessionLocal factory for creating database sessions. 
# Here, Base is a declarative base for defining SQLAlchemy models which we use to create our databse model(named Item).
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()