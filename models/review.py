#!/usr?bin?python3
"""New class from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review 'a class' that inherits from BaseModel 
        Attributes:
            place_id (str): ID of the place
            user_id (str): ID of user who wrote the review
            text (str): Text content of the review
        """
    place_id = ""
    user_id = ""
    text = ""