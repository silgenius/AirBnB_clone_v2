#!/usr/bin/python3

"""
    Module: review

    This module implements the Review class, which inherits from BaseModel
    and Base respectively.
"""

from models.base_model import BaseModel
from sqlachemy import Colunm, String, ForeignKey 

class Review(BaseModel, Base):
    """
    This class represents a review for a place.
    """
    __tablename__ = 'reviews'
    place_id = Colunm(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Colunm(String(60), ForeignKey('users.id'), nullable=False)
    text =  Colunm(String(1024), nullable=False)
