#!/usr/bin/python3

"""
    Module: user

    This module implements the User class, which inherits from BaseModel
    and base respectively.
"""

from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel):
    """
    This class represents a user with email, password, first name,
    and last name attributes.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        All attributes defaults to an empty string.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship(
            "Place",
            cascade="all, delete, delete-orphan",
            backref="user"
            )
    reviews = relationship(
            "Review",
            cascade="all, delete, delete-orphan",
            backref="user"
            )

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.
        """
        super().__init__(*args, **kwargs)
