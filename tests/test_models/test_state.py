#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.city import City
import os

class TestState(TestBasemodel):
    """Test model for state"""

    def __init__(self, *args, **kwargs):
        """Test calls Initialization"""
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def TestName(self):
        """Type of name testing"""
        n = self.value()
        self.assertEqual(type(n.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
