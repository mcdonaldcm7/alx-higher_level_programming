#!/usr/bin/python3
"""
A module that uses SQLAlchemy to access and the database passed, and makes
queries to perform the specified operation
"""


import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


Base = declarative_base()


class State(Base):
    """
    State class:
        - inherits from 'Base'
        - links to the MySQL table 'states'
        - class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        -class attribute name that represents a column of a string with
        maximum 128 characters and can’t be null
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)


class City(Base):
    """
    City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - id represents a column of an auto-generated, unique integer,
        can’t be null and is a primary key
        - name represents a column of a string of 128 characters and
        can’t be null
        - state_id represents a column of an integer, can’t be null and is a
        foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")


if __name__ == "__main__":
    usr = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        usr, psswd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(City).order_by(City.id)
    for instance in instances:
        print("{}: {} -> {}".format(
            instance.id, instance.name, instance.state.name))
    session.commit()
    session.close()
