#!/usr/bin/python3
"""This module serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json


class FileStorage:
    """ a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        keys = f"{type(obj).__name__}.{obj.id}"
        self.__objects[keys] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key, values in data.items():
                class_name = values['__class']
                obj = eval(class_name)(**values)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
