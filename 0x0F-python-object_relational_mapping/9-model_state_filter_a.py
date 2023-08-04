#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""


from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    """
    connect and interact with the database to retrieve
    the specified result
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()

    if query is not None:
        for q in query:
            print("{}: {}".format(q.id, q.name))
