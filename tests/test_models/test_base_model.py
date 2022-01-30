#!/usr/bin/python3
"""
BaseModel test
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
import pep8
"""
Test case for base_model
"""


class TestBase(unittest.TestCase):
    """Tests for class BaseModel"""
    def test_for_style(self):
        """style test"""
        style = pep8.StyleGuide(quiet=True)
        chk = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(chk.total_errors, 0, "fix pep8")

    def test_attributes_type(self):
        """Test id is str"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_dict(self):
        """Test for instance to dictionary"""
        my_model = BaseModel()
        my_model.name = "My first Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIn('my_number', my_model_json)
        self.assertIn('name', my_model_json)
        self.assertIn('__class__', my_model_json)
        self.assertIn('updated_at', my_model_json)
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        """Test for Base Model"""

    def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """check if attributes exists"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_baseModel_dict(self):
        """Test the re-crated instsnace with the dictionary"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertNotIn('__class__', my_new_model.__dict__)
        self.assertIn('name', my_new_model.__dict__)
        self.assertIn('id', my_new_model.__dict__)
        self.assertIn('my_number', my_new_model.__dict__)
        self.assertIn('updated_at', my_new_model.__dict__)
        self.assertIn('created_at', my_new_model.__dict__)
        created_type = type(my_new_model.created_at)
        self.assertEqual(created_type, datetime)
        updated_type = type(my_new_model.updated_at)
        self.assertEqual(updated_type, datetime)

    def test_datetime(self):
        """
        Tests for correct datetime format
        """

if __name__ == '__main__':
    unittest.main()
