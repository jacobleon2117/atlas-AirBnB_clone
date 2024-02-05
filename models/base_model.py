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

    def save(self):
        """
        """
        self.updated_at = datetime.utcnow

    def __str__(self):
        name = type(self).__name__
        return "[{0}] ({1}) {2}".format(name, self.id, self.__dict__)

    def to_dict(self):
        """
        """
        inst_dict = self.__dict__.copy()