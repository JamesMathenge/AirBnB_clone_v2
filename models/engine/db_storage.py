#!/usr/bin/python3
"""New Database Engine"""

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f'mysql+mysqldb: // {environ.get("HBNB_MYSQL_USER")}:
                {environ.get("HBNB_MYSQL_PWD")
                 }@{environ.get("HBNB_MYSQL_HOST")}
                / {environ.get("HBNB_MYSQL_DB")}',
            pool_pre_ping=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import storage
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for class_name in storage.classes:
                objects.extend(self.__session.query(
                    storage.classes[class_name]).all())

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(
            self.__engine)
        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(
            Session)
