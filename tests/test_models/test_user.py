#!/usr/bin/python3
"""Test module"""
import unittest
import models
from models.user import User
from datetime import datetime


class TestUserModel(unittest.TestCase):
    """Unittest for testing User class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User().email))

    def test_password(self):
        self.assertEqual(str, type(User().password))

    def test_first_name(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User().last_name))

    def test_two_user(self):
        new_user1 = User()
        new_user2 = User()
        self.assertNotEqual(new_user1.id, new_user2.id)


class TestUserModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the User class"""

    def test_to_dict(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_keys(self):
        new_user = User()
        self.assertIn("id", new_user.to_dict())
        self.assertIn("created_at", new_user.to_dict())
        self.assertIn("updated_at", new_user.to_dict())
        self.assertIn("__class__", new_user.to_dict())

    def test_to_dict_attributes(self):
        new_user = User()
        new_user.my_number = 123
        self.assertIn("my_number", new_user.to_dict())

    def test_to_dict_datetime_str(self):
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))
        self.assertEqual(str, type(user_dict["id"]))

    def test_contrast_dict(self):
        new_user = User()
        self.assertNotEqual(new_user.to_dict(), new_user.__dict__)


if __name__ == "__main__":
    unittest.main()
