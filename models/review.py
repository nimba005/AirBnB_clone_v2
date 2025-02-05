#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base, Column, String
import os
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship('User', back_populates='reviews')
        place = relationship('Place', back_populates='reviews') # cascade? slave

    else:
        place_id = ""
        user_id = ""
        text = ""
