#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def all(self):
        return self.__objects

    def new(self, obj):
        keys = f"{type(obj).__name__}.{obj.id}"
        self.__objects[keys] = obj

    def save(self):
        serialized_data = {}
        for key, val in self.__objects.items():
            serialized_data[key] = val
        with open(self.__file_path, 'w') as file:
            json.dumps(serialized_data, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load()
            for key, values in data.items():
                self.__objects[key] = eval(values['__class'])(**values)
        except FileNotFoundError:
            pass
