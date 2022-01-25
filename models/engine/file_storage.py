#!/usr/bin/python3
"""import modules"""
import json
from models.base_model import BaseModel
import os.path

class FileStorage():
    """To serialize instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "/root/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj.id = self.__obects

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, "w") as x1:
            json.dump(self.__objects, x1)

    def reload(self):
        """deserializes the JSON file to __objects only if
        the JSON file exists: otherise, do nothing
        no exception should be raised"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as x:
                json.load(x)
        else:
            pass
