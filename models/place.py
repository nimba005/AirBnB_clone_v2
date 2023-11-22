#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Float, Table
from models.base_model import Integer, ForeignKey

place_amenity = Table('place_amenity', Base.metadata,
                       Column('place_id', String(60),
                               ForeignKey('place.id'), nullable=False),
                       Column('amenity_id', String(60),
                               ForeignKey('amenities.id'), nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullagle=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullagle=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship(
            'Reviews', back_populates='place',
            cascade='all, delete, delete-orphan')
        user = relationship(
            'User', back_populates='places') # cascade? slave
        amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False, back_populates='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Review getter - return list of filtered reviews. """
            reviews_instances = []
            reviews_dict = models.storage.all('Review')
            for key, value in reviews_dict.items():
                if self.id == value.place_id:
                    reviews_instances.append(value)
            return reviews_instances
        @property
        def amenities(self):
            """Review getter - returns list of amenity instances"""
            return self.amenity_ids
        @amenities.setter
        def amenities(self, obj):
            """Setter for amenity list"""
            if isinstance(obj, Amenity):
                self.ammenity_ids.append(obj.id)
