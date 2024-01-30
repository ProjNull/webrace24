from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

    Id = Column(
        Integer, 
        nullable=False,
        unique=True, 
        primary_key=True, 
        autoincrement=True
    )
    firstName = Column(
        String, 
        nullable=False,
    )
    lastName = Column(
        String, 
        nullable=False,
    )
    email = Column(
        String, 
        nullable=True, 
        unique=True
    )
    phone = Column(
        Integer, 
        nullable=True
    )
    githubUrl = Column(
        String, 
        nullable=True
    )
    preferences = Column(
        String, 
        nullable=True
    )
    message = Column(
        String, 
        nullable=True,
    )
    other = Column(
        String, 
        nullable=True
    )