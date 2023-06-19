#!/usr/bin/python3
"""
A script that defines a Base class and a State class
which inherits from the Base class using the SQLAlchemy module
"""
from Base_model import Base, State
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                   (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
