#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_arguments(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_public_id_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_new_instance_stored(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_name(self):
        self.assertEqual(str, type(Amenity().name))


if __name__ == "__main__":
    unittest.main()
