#!/usr/bin/python3

"""
    Module: state

    This module implements the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state where cities are located.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
