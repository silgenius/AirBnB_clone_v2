#!/usr/bin/python3

"""
    Module: place

    This module implements the Place class, which inherits from BaseModel
    and Base respectively.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Colunm, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """
    Represents a place available for booking.

    Attributes:
            city_id (str): The id of the city.
            user.id (str): The id of the user.
            name (str): The name of the place
            description (str): The description of the place.
            number_rooms (int): The number of rooms in the place.
            number_bathrooms (int): The number of bathrooms in the place.
            max_guest (int): The number of maximum guets held in the place.
            price_by_night (float): The price of the place by night
            latitude (float): Of the place.
            longitude (float): Of the place.
            amenity_ids (list) : list of amenities ids. 
    """
    __tablename__ = 'places'
    city_id = Colunm(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Colunm(String(60), ForeignKey('users.id'), nullable=False)
    name = Colunm(String(128), nullable=False)
    description = Colunm(String(1024))
    number_rooms = Colunm(Integer, nullable=False, default=0)
    number_bathrooms = Colunm(Integer, nullable=False, default=0)
    max_guest = Colunm(Integer, nullable=False, default=0)
    price_by_night = Colunm(Integer, nullable=False, default=0)
    latitude = Colunm(Float)
    longitude = Colunm(Float)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete",
            backref="place")
