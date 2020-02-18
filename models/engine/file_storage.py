#!/usr/bin/python3
"""FileStorage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

import models


class FileStorage:
    """
        ------------------------------------------------------
        class FileStorage that serializes instances
        to a JSON file and deserializes JSON file to instances
        ------------------------------------------------------
    """
    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # store all objects
    name_class = {}

    def all(self):
        """
            --------------------------------
            returns the dictionary __objects
            --------------------------------
        """
        return self.__objects

    def new(self, obj):
        """
            ------------------------------------------------------
            sets in __objects the obj with key <obj class name>.id
            ------------------------------------------------------
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
            -------------------------------------
            serializes __objects to the JSON file
            -------------------------------------
        """
        dict_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, 'w') as files:
            files.write(json.dumps(dict_json))

    def reload(self):
        """
            ---------------------------------------------------
            deserializes the JSON file to __objects
            only if the JSON file exists; otherwise, do nothing
            ---------------------------------------------------
        """
        try:
            with open(self.__file_path, 'r') as files:
                from_json = json.loads(files.read())
                for key, value in from_json.items():
                    name_class = key.split(".")
                    copy = globals()[name_class[0]](**value)
                    self.__objects[key] = copy
        except IOError:
            pass
