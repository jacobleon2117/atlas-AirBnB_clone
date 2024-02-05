#!/usr/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that repersents Amenity inhertied from Basemodel
        Attributes:
            name (str): the name of amenity
    """
    name = ""