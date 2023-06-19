#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database to retrieve the desired result
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Add the new state object"""
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """query the database"""
    state = session.query(State).order_by(State.id).all()

    if state is not None:
        for s in state:
            print('{}: {}'.format(s.id, s.name))
    session.close()
