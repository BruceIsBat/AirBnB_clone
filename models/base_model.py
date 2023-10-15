#!/usr/bin/python3
"""This module contains the Basemodel class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A class BaseModel that defines
    all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """The constructor assign uuid to an instance id
        and datetime to create_a

        Args:
            *args: a tuple
            **kwargs: a dictionary input
        """
        if kwargs:
            t_form = '%Y-%m-%dT%H:%M:%S.%f'
            for key, values in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(values, t_form))
                    else:
                        setattr(self, key, values)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
            storage.new()
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())

    def __str__(self):
        """The string representation of the Basemodel

        Returns:
            [BaseModel] ({self.id}) {self.__dict__}
        """

        return "[BaseModel] ({}) {} ".format(self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute
        updated_at with the current datetime
        """

        storage.save(self)
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Serialize and returns
        dictionary containing all keys/values of __dict__ of the instance

        Returns:
            returns a dictionary containing all keys/values
        """

        data = self.__dict__.copy()
        data['__class'] = type(self).__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.created_at.isoformat()

        return data
