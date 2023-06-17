#!/usr/bin/python3
"""
This module makes use of the SQLAlchemy library access and query the database
name passed as an argument to the command line.
It import and uses the table defined by State to make it queries
"""


import sys
from model_state import Base, State
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
    query = session.query(State).filter(State.name.like("%a%"))
    records = query.all()
    for record in records:
        session.delete(record)
    session.commit()
