#!/usr/bin/python3
"""
This file contains the definition for the City class which inherits from Base
imported from 'model_state'
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - id represents a column of an auto-generated, unique integer,
        can’t be null and is a primary key
        - name represents a column of a string of 128 characters and
        can’t be null
        - state_id represents a column of an integer, can’t be null and is a
        foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
