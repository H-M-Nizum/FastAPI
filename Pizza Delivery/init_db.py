# For Automated Create Database Table Using ORM

from database import engine, Base
from models import UsersModel, PizzaModel, OrderModel

Base.metadata.create_all(bind=engine)
