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
        
