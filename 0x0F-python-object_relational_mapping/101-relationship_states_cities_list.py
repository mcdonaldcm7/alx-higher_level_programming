#!/usr/bin/python3
"""
A module that uses SQLAlchemy to access and the database passed, and makes
queries to perform the specified operation
"""


import sys
from relationship_city import City
from relationship_state import Base, State
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

    instances = session.query(State).order_by(State.id)
    for instance in instances:
        print("{}: {}".format(instance.id, instance.name))
        for city in instance.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.commit()
    session.close()
