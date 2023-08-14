#!/usr/bin/python3
'''
Module Docs
'''
from json import dumps, loads
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    Class Docs
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Docs
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Docs
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Docs
        '''
        final_dict = {
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        json_string = dumps(final_dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        '''
        Docs
        '''
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        filename = FileStorage.__file_path
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                final_dict = loads(json_string)
            for key, value in final_dict.items():
                class_name, obj_id = key.split(".")
                if class_name in allowed_classes:
                    eval("self.new({}(**value))".format(class_name))
