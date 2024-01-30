from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "Admins"

    Id = Column(
        Integer, 
        nullable=False,
        unique=True, 
        primary_key=True, 
        autoincrement=True
    )
    email = Column(
        String, 
        nullable=False, 
        unique=True
    )
    password = Column(
        String, 
        nullable=False
    )