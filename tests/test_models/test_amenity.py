#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity
import os
import sys

class TestAmenity(TestBasemodel):
    """Represent the test for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """TEST CLASS INIT."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """NAME TYPE TESTING."""
        n = self.value()
        self.assertEqual(
            type(n.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
