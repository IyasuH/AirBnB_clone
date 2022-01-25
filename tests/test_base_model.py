#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.base_model import BaseModel
"""
Test case for BaseModel
"""


class TestBase(unittest.TestCase):
    def test_id(self):
        """Test id is str"""
        my_model = BaseModel()
        id_type = type(my_model.id)
        self.assertEqual(id_type, str)

    def to_dict(self):
        """Test for instance to dictionary"""
        my_model = BaseModel()
        my_model.name = "My first Model"
        my_model.my_number = 89
        my_model_json = b.to_dict()
        self.assertIn('my_number', my_model_json)
        self.assertIn('name', my_model_json)
        self.assertIn('__class__', my_model_json)
        self.assertIn('updated_at', my_model_json)
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        """Test for Base Model"""

if __name__ == '__main__':
    unittest.main()
