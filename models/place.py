#!/usr/bin/python3

"""
    Module: place

    This module implements the Place class, which inherits from BaseModel
    and Base respectively.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


"""
    This is a Table for creating the relationship
    Many-To-Many between Place and Amenity 
    attributes: 
    place_id (str):the id of the place never NULL.
    amenity_id (str): the id of the amenity never NULL.
"""
place_amenity = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                        ForeignKey("places.id"),
                        primary_key=True, nullable=False),
                        Column("amenity_id", String(60),
                        ForeignKey("amenities.id"),
                        primary_key=True, nullable=False))




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

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete",
            backref="place")
    amenities = relationship("Amenity",
            secondary="place_amenity",
            viewonly=False,
            backref="palce_amenities"
            )



    if getenv('HBNB_TYPE_STORAGE') !='db':
        @property
        def reviews(self):
            """This is a getter attribute reviews that returns the list
            of Review instances with place_id equals to the current Place.id"""

            from models import storage


            review_insts = storage.all(Review)
            for review in review_insts.values():
                if review.place_id == self.id:
                    return review


    @property
    def amenities(self):
        """ A function  that returns a list of amenity ids """
        
        return self.amenity_ids

    @amenities.setter
    def amenities(self, inst=None):
        """ This is a Setter attribute amenities that 
        handles append method of amenity id to ids list."""

        if type(inst) is Amenity and inst.id not in self.amenity_ids:
            self.amenity_ids.append(inst.id)
