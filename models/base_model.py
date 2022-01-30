#!/usr/bin/python3
"""
contains Base model which defines all common
attributes/methods for other classes
"""

from datetime import datetime
import models
import uuid
"""Base Model"""


class BaseModel():
    """
    Baseclass
    base for all the classes in the which defines
    all common attributes/method for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        public instance attributes
        Args:
            *args(args): arguments
            **kwargs(dict): attribute values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
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
        """
        update the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        return dict_copy
