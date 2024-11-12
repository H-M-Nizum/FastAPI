# from ..database import Base
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship



class PizzaModel(Base):
    
    PIZZA_SIZE=(
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    )
    __tablename__ = 'pizza'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    size = Column(ChoiceType(choices=PIZZA_SIZE), default='SMALL')
    price = Column(Integer, nullable=True)
    
    orders = relationship('OrderModel', back_populates='pizza')
    
    
    def __str__(self):
        return f"<User {self.name}>"
    

class OrderModel(Base):
    
    ORDER_STATUS=(
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )
    
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, default=1)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default='PENDING')
    user_id = Column(Integer, ForeignKey("users.id"))
    pizza_id = Column(Integer, ForeignKey("pizza.id"), )

    users = relationship("UsersModel", back_populates="orders")
    pizza = relationship("PizzaModel", back_populates="orders")
    def __str__(self):
        return f"<User {self.user_id} - {self.pizza_id}>"
    