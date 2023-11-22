#!/usr/bin/python3
"""
This module defines a class User
"""
import os
from models.base_model import BaseModel, Base, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    """
    __tablename__ = 'users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
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
