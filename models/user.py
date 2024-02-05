#!/usr/bin/python3
"""New class from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User 'a class' that inherits from BaseModel
        
        Attributes:
            email (str): The user's email
            password (str): The user's password
            first_name (str): The user's first name
            last_name (str): The user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""