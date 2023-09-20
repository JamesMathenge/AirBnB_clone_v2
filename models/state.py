#!/usr/bin/python3
"""Module for the State class in the HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
import os


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
