#!/usr/bin/python3
""" unittest for Amenity class"""
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pep8

class Test(unittest.TestCase):
    def test_for_style(self):
        """style test"""
        style = pep8.StyleGuide(quiet=True)
        chk = style.check_files(['models/amenity.py'])
        self.assertEqual(chk.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_type(self):
        """check that class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

if __name__== '__main__':
    unittest.main()
