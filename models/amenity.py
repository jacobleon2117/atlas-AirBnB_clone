#!/usr/python3

from models.base_model import base_model


class Amenity(BaseModel):
    """Class that repersents Amenity inhertied from Basemodel
        Attributes:
            name (str): the name of amenity
    """
    name = ""