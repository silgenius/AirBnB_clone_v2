#!/usr/bin/python3

"""
    Module: db_storage

    This module implements the New engine DBStorage, which facilitates the
    stoorage of data into database.
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import session.maker
from os import getenv
from .models.city import City
from .models.state import State
from .models.review import Review
from .models.place import Place
from .models.amenity import Amenity
from .models.user import User


class DBStorage:
    __engine = None
    __session = None

    password = getenv('HBNB_MYSQL_PWD')
    username = getenv('HBNB_MYSQL_USER')
    database = getenv('HBNB_MYSQL_DB')
    localhost = getenv('HBNB_MYSQL_HOST')
    env = getenv('HBNB_ENV')

    def __init__(self):
        self.__engine = create_engine(f'mysql+mymsqldb://{username}:\
                {password}@{localhost}/{database}', pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        if cls:
            cls_list = []
            cls_liat.append(cls)
        else:
            cls_list = [User, State, City, Amenity, Place, Review]
        for cls in cls_list:
            data = self.__session.query(cls)
            for result in results:
                key = result[0].__class.__name + "." + result[0].id
               new_dict[key] = result[0].to_dict()

    def new(self, obj):
        self.__session(obj)

    def save(self):
        session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
