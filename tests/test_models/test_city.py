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
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the Place class."""

    def test_no_arguments(self):
        self.assertEqual(City, type(City()))

    def test_public_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name(self):
        self.assertEqual(str, type(City().name))

    def test_state_id(self):
        self.assertEqual(str, type(City().state_id))
