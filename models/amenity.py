#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

""" State Module for HBNB project """

"""from models.base_model import BaseModel

class Amenity(BaseModel):
    name = "";
"""

"""This is the amenity class"""


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
