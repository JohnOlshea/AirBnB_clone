#!/usr/bin/python3
"""Test module"""
import unittest
import models
from models.state import State
from datetime import datetime


class TestStateModel(unittest.TestCase):
    """Unittest for testing State class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        new_state = State()
        self.assertEqual(str, type(State().name))
        self.assertNotEqual("name", new_state.__dict__)
        self.assertIn("name", dir(new_state))

    def test_two_state(self):
        new_state1 = State()
        new_state2 = State()
        self.assertNotEqual(new_state1.id, new_state2.id)


class TestStateModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the State class"""

    def test_to_dict(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_keys(self):
        new_state = State()
        self.assertIn("id", new_state.to_dict())
        self.assertIn("created_at", new_state.to_dict())
        self.assertIn("updated_at", new_state.to_dict())
        self.assertIn("__class__", new_state.to_dict())

    def test_to_dict_attributes(self):
        new_state = State()
        new_state.my_number = 123
        self.assertIn("my_number", new_state.to_dict())

    def test_to_dict_datetime_str(self):
        new_state = State()
        state_dict = new_state.to_dict()
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))
        self.assertEqual(str, type(state_dict["id"]))

    def test_contrast_dict(self):
        new_state = State()
        self.assertNotEqual(new_state.to_dict(), new_state.__dict__)


if __name__ == "__main__":
    unittest.main()
