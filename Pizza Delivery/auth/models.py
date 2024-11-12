from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

class UsersModel(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    
    orders = relationship('OrderModel', back_populates='users')
    
    def __str__(self):
        return f"<User {self.username}>"
    