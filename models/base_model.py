#!/usr/bin/python3
"""
    ---------------
    class BaseModel
    ---------------
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """
        ---------------------------------------
        class BaseModel that defines all common
        attributes/methods for other classes
        ---------------------------------------
    """
    my_dict = {}

    def __init__(self, *args, **kwargs):
        """
            -------------------------------------------------------------
            constructor BaseModel
            id: assign with an uuid when an instance is created
            created_at: assign with the current datetime
                        when an instance is created
            updated_at: assign with the current datetime
                        when an instance is created and it
                        will be updated every time you change your object
            -------------------------------------------------------------
        """
        if len(kwargs) != 0:
            """
                -------------------------------------------------
                if kwargs is not empty
                each key of this dictionary is an attribute name
                __class__ from kwargs is the only one that should
                 not be added as an attribute
                -------------------------------------------------
            """
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    """
                        --------------------------------
                        change format string to datetime
                        --------------------------------
                    """
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
            --------------------------------------------------------
            should print: [<class name>] (<self.id>) <self.__dict__>
            --------------------------------------------------------
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            -------------------------------------
            updates the public instance attribute
            updated_at with the current datetime
            -------------------------------------
        """
        setattr(self, "updated_at", datetime.now())
        models.storage.save()

    def to_dict(self):
        """
            -----------------------------------------------
            returns a dictionary containing all keys/values
            of __dict__ of the instance
            -----------------------------------------------
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
