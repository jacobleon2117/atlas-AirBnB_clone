#!/usr/bin/python3
"""New class from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State 'a class' that inherits from BaseModel
        Attributes:
            name (str): The name of the State
        """

    name = ""
