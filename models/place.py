#!/usr/bin/python3
"""New class from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place 'a class' that inherts from BaseModel
        Attributes:
            city_id (str): ID for city of the place location
            user_id (str): ID for owner user of the place
            name (str): Name of place
            description (str): Description of the place
            number_rooms (int): Number of rooms
            number_bathrooms (int): Number of bathrooms
            max_guest (int): Mx number of guests
            price_by_night (int): Price per night of stay
            latitude (float): Latitude coordinate
            longitude (float): Longitude coordinate
            amenity_ids (list): List of amenity IDs
        """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
