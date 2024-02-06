#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Model for class Base
    """
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "upated_at":
                    setattr(self.key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def save(self):
        """
        """
        self.updated_at = datetime.utcnow
        models.storage.save()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
