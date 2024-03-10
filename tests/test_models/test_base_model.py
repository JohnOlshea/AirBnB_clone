#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_instantiation(self):
        """
        Tests that a BaseModel instance is created
        with the correct attributes.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_save(self):
        """
        Test the save method.
        updated_at before save should not equal udated_at after save
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        expected_keys = [
            'id', 'created_at', 'updated_at',
            '__class__', 'name', 'my_number'
        ]
        self.assertEqual(sorted(model_dict.keys()), sorted(expected_keys))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertEqual(model_dict['name'], 'My First Model')
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(type(model_dict["created_at"]), str)
        self.assertEqual(type(model_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
