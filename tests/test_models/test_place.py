#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place
import os

class TestPlace(TestBasemodel):
    """TEST CLASS"""

    def __init__(self, *args, **kwargs):
        """INIT THE TEST CLASS"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        n = self.value()
        self.assertEqual(type(n.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """USER_ID TESTING"""
        n = self.value()
        self.assertEqual(type(n.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """NAME TYPE TESTING"""
        n = self.value()
        self.assertEqual(type(n.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """DESCRIPTION TESTING"""
        n = self.value()
        self.assertEqual(type(n.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """ROOM NUMBER TESTING"""
        n = self.value()
        self.assertEqual(type(n.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
        """BATHROOMS NUMBER TESTING"""
        n = self.value()
        self.assertEqual(type(n.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest(self):
        """MAX_GUEST TEST"""
        n = self.value()
        self.assertEqual(type(n.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night(self):
        """PRICE BY NIGHT TESTING"""
        n = self.value()
        self.assertEqual(type(n.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude(self):
        """LATITUDE TESTING"""
        n = self.value()
        self.assertEqual(type(n.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude(self):
        """LONGITUDE TESTING"""
        n = self.value()
        self.assertEqual(type(n.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """AMENITY ID TESTING"""
        n = self.value()
        self.assertEqual(type(n.amenity_ids), list)
