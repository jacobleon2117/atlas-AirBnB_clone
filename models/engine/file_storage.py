#!/usr/bin/python3

import json
import os
from os.path import isfile

class FileStorage:
    """
    obj takes
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Takes passed args then stores 
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns filestorage
        """
        return FileStorage.__objects
    
    def save(self):
        """
        Save to json format for storing 
        """
        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage._object[key] = instance
                except Exception:
                    pass