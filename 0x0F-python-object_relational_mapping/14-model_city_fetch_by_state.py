#!/usr/bin/python3
"""
This module makes use of the SQLAlchemy package to access the database passed
as a parameter and make a query (Fetch all City objects from the database)
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, psswd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City, State).join(State).order_by(City.id):
        print("{}: ({}) {}".format(
            instance.State.name, instance.City.id, instance.City.name))
