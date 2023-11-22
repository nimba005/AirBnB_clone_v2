#!/usr/bin/python3
"""
This module defines a class User
"""
from models.base_model import BaseModel
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    """
    __tablename__ = 'users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        username = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)

        places = relationship(
            'Place', back_populates='user',
            cascade='all, delete, delete-orphan')
        reviews = relationship(
            'Review', back_populates='user',
            cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
