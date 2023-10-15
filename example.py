#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model.id)
print(type(my_model.created_at))
print(type(my_model))
my_model.save()
print()
print(my_model)
my_model_json = my_model.to_dict()
print()
print(my_model_json)
print(type(my_model_json))
print()
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))
