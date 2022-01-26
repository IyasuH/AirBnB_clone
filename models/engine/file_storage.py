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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        with open(FileStorage.__file_path, "w") as x1:
            json.dump(FileStorage.__objects, x1)

    def reload(self):
        """deserializes the JSON file to __objects only if
        the JSON file exists: otherise, do nothing
        no exception should be raised"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as x:
                json.load(x)
        else:
            pass
