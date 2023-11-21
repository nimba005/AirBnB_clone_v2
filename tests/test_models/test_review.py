#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.city import City
import os

class TestState(TestBasemodel):
    """Test models for state"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def TestPlaceId(self):
        """Test [place id]"""
        n = self.value()
        self.assertEqual(type(n.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def TestUserId(self):
        """Test user"""
        n = self.value()
        self.assertEqual(type(n.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def TestText(self):
        """Test text"""
        n = self.value()
        self.assertEqual(type(n.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
