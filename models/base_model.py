#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            kwargs (dict): Key-value pairs of attributes to set.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            elif key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.strptime(value, time_format))
            else:
                setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        Saves the current instance to the storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary.

        Returns:
            dict: Dictionary representation of the instance.
        """
        inst_dict = {
            key: value.isoformat() if isinstance(value, datetime) else value
            for key, value in self.__dict__.items()
        }
        inst_dict["__class__"] = self.__class__.__name__

        return inst_dict

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
