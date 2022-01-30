#!/usr/bib/python3
"""
include modules
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8


class TestFileStorage(unittest.TestCase):
    """FileStorage Test class"""
    def test_for_style(self):
        """style test"""
        style = pep8.StyleGuide(quiet=True)
        chk = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(chk.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == '__main__':
    unittest.main()
