#!/usr/bin/python3

"""
    Module: state

    This module implements the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from city import City

class State(BaseModel, Base):
    """
    Represents a state where cities are located.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
    
    @property
    def cities(self):
        all_cities = storage.all(City)
        all_cities = [city for city in all_cities.get_values() if city.state_id == self.id]
        return all_cities
