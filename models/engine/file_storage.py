#!/usr/bin/python3
"""
To manage files as JSON file
"""
import json
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path
"""File Storage"""


class FileStorage():
    """
    To serialize instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path)
        """
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w+", encoding='utf-8') as x:
            x.write(json.dumps(json_dict))

    def reload(self):
        """deserializes the JSON file to __objects only if
        the JSON file exists: otherwise, do nothing
        no exception should be raised"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r",
                      encoding='utf-8') as x:
                dict_back = json.loads(x.read())
                for k, v in dict_back.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
        else:
            pass
