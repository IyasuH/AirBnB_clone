#!/usr/bin/python3
"""import modules"""
from datetime import datetime
import json
import models
import uuid
"""Base Model"""


class BaseModel():
    """Baseclass"""
    def __init__(self, *args, **kwargs):
        """public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs[key]
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ method to return [<class name>]
        (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dict_copy = dict(self.__dict__)
        dict_copy['id'] = self.id
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        return (dict_copy)
