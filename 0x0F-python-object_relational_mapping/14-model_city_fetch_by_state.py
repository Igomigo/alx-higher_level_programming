#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""


from model_city import City
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """
    Connecting to the database to perform some operations
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database"""
    cities = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """Commit the session"""
    session.commit()
    session.close()
