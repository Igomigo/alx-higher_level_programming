#!/usr/bin/python3
"""
This file contains the definition of the City class mapped
to the database with the sqlalchemy ORM
"""


from sqlalchemy import Integer, Column, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    The City class.

    Attributes:
         __tablename__: Name of the table in the database.
         id(Int): represents a column of an auto-generated,
                unique integer, can’t be null and is a primary key.
         name(String): represents a column of a string of 128
                characters and can’t be null.
         state_id(Int): represents a column of an integer, can’t be null
                and is a foreign key to states.id.
    """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(128))
    state_id = Column(Integer, nullable=False, ForeignKey('State.id'))
