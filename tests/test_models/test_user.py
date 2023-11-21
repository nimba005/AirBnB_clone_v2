#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.user import User
import os
from sqlalchemy import Column

class TestUser(TestBasemodel):
    """Represent the tests for the user model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the type of first_name"""
        n = self.value()
        self.assertEqual(type(n.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_last_name(self):
        """Test the type of last_name"""
        n = self.value()
        self.assertEqual(type(n.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_email(self):
        """Test the type of password."""
        n = self.value()
        self.assertEqual(type(n.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_password(self):
        """Test the type of password"""
        n = self.value()
        self.assertEqual(type(n.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
