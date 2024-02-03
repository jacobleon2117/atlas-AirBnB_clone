#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """
    Model for class Base
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def to_dict