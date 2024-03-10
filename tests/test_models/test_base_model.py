#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_save(self):
        """
        Test the save method.
        updated_at before save should not equal udated_at after save
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

if __name__ == '__main__':
    unittest.main()        
