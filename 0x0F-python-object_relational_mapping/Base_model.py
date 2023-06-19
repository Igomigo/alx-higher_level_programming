#!/usr/bin/python3
"""
Script that defines a class mapped to a database
using the MySQLAlchemy object relational mapper(ORM)
"""


from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

     Attributes:
         __tablename__ (str): The table name in the database
         id (int): The State id of the class
         name (str): The State name of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, auto_generated, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
