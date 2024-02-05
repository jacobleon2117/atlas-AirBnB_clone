#!/usr/bin/python3
"""
Contians class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """BaseModel class future classes will derive from"""
    def __int__(self, *args, **kwargs):
        """ Initialization for BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("update_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.update_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name, self.id,
                                        self.__dict__)

def save(self):
    """Attribute for 'updated_at' with current datetime"""
    self.updated_at = datetime.utcnow()
    models.storage.new(self)
    models.storage.save()

def to_dict(self, save_fs=None):
    """A dictionary containing all keys/values of the instance"""
    new_dict = self.__dict__.copy()
    if "created_at" in new_dict:
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
    if "updated_at" in new_dict:
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
    new_dict["__class__"] = self.__class__.__name__
    if "_sa_instance_state" in new_dict:
        del new_dict["_sa_instance_state"]
    if save_fs is None:
        if "password" in new_dict:
            del new_dict["password"]
    return new_dict

def delete(self):
    """current instance is deleted from storage"""
    models.storage.delete(self)