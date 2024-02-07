#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for city that inherits from BaseModel
    Attributes:
        state_id (str): Id of the state the city belongs
        name (str): Name of the city
    """

    state_id = ""
    name = ""
