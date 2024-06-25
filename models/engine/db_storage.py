#!/usr/bin/python3

"""
    Module: db_storage

    This module implements the New engine DBStorage, which facilitates the
    stoorage of data into database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        password = getenv('HBNB_MYSQL_PWD')
        username = getenv('HBNB_MYSQL_USER')
        database = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}/{database}', pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            cls_list = []
            cls_liat.append(cls)
        else:
            cls_list = [State, City]
        new_dict = {}
        for cls in cls_list:
            result = self.__session.query(cls.id).first()
            if result:
                key = "State" + "." + result[0]
                new_dict[key] = result[0]
        return new_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
