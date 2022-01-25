#!/usr/bin/python3
"""import modules"""
import json
from models.base_model import BaseModel
import os.path

class FileStorage():
    """To serialize instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = ""
    __objects = {}
    def all(self):
        """returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.obj = BaseModel.id

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        with open("__file_path", "w") as x:
            json.dump(__objects, x)

    def reload(self):
        """deserializes the JSON file to __objects only if
        the JSON file exists: otherise, do nothing
        no exception should be raised"""
        if os.path.exists(__file_path):
            with open(__file_path, mode='r') as x:
                json.load(__file_path)
        else:
            pass
