#!/usr/bin/python3
"""import modules"""
from datetime import datetime
import json
import uuid

class BaseModel():
    """Baseclass"""

    def __init__(self, *args, **kwargs):
        """public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            from models import storage
            storage.new()

    def __str__(self):
        """__str__ method to return [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute
        updated_at with the current datetime"""
        from models import storage
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        self.__dict__['updated_at'] = datetime.now().isoformat()
        self.__dict__['created_at'] = datetime.now().isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return (self.__dict__)
