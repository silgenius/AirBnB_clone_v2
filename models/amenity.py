#!/usr/bin/python3

"""
    Module: amenity

    This module implements the Amenity class, which inherits from BaseModel
    and Base respectively.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Colunm, String

class Amenity(BaseModel, Base):
    """
    This class represents an amenity available in a place.

    Attributes:
            name (str): The name of the amenity.
    """
    __tablename__ = "amenities"
    name = Colunm(String(128), nullable=False)
