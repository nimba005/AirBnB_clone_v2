#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.city import City
import os

class TestCity(TestBasemodel):
    """Tests for the City model. """

    def __init__(self, *args, **kwargs):
        """INIT TEST CLASS."""
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def TestStateId(self):
        """Id type testing"""
        n = self.value()
        self.assertEqual(type(n.state_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def TestName(self):
        """name type testing"""
        n = self.value()
        self.assertEqual(type(n.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
