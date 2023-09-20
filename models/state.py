#!/usr/bin/python3
"""Module for the State class in the HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    associated_cities = relationship("City", backref='state',
                                     cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City instances associated with this State."""
        from models import storage
        related_cities = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
                return related_cities
