#!/usr/bin/python3
""" CITY MODEL """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base

class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    __tablename__ = 'cities'
    state_id = Column(
            String(60), ForeignKey('states.id'), nullable=False
            ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
            String(128), nullable=False
            ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place', cascade='all, delete, delete-orphan', backref='cities'
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
