#!/usr/bin/python3
"""Test for Place"""
from models.place import Place
from models.base_model import BaseModel
import unittest
import pep8
from datetime import datetime


class Test(unittest.TestCase):
    def test_for_style(self):
        """style test"""
        style = pep8.StyleGuide(quiet=True)
        chk = style.check_files(['models/place.py'])
        self.assertEqual(chk.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_type(self):
        """check that class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
