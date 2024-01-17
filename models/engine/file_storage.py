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
        keys = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[keys] = obj

    def save(self, obj=None):
        """serializes __objects to the JSON file
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = file.read()
                if data:
                    data = json.loads(data)
                    for key, values in data.items():
                        if '__class' in values:
                            class_name = values.pop('__class')
                            obj = globals()[class_name](**values)
                            self.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON file: {e}")


if __name__ == "__main__":
    FileStorage()
