from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

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
        nullable=False, 
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
    other = Column(
        String, 
        nullable=True
    )

    # firstName: string;
    # lastName: string;
    # email?: string;
    # phone?: string;
    # githubUrl?: string;
    # preferences?: "Backend" | "Frontend" | "Fullstack" | "Design" | "Project Management";

    # other?: any;