#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""


from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    """
    interact with the database to retrieve the specified result
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).first()
    if query is not None:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
