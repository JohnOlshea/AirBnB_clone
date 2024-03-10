#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestPlace_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_arguments(self):
        self.assertEqual(Place, type(Place()))

    def test_public_id_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id(self):
        self.assertEqual(str, type(Place().city_id))

    def test_user_id(self):
        self.assertEqual(str, type(Place().user_id))

    def test_name(self):
        self.assertEqual(str, type(Place().name))

    def test_description(self):
        self.assertEqual(str, type(Place().description))

    def test_number_rooms(self):
        self.assertEqual(int, type(Place().number_rooms))

    def test_number_bathrooms(self):
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_max_guest(self):
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night(self):
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude(self):
        self.assertEqual(float, type(Place().latitude))

    def test_longitude(self):
        self.assertEqual(float, type(Place().longitude))

    def test_amenity_ids(self):
        self.assertEqual(list, type(Place().amenity_ids))


if __name__ == "__main__":
    unittest.main()
