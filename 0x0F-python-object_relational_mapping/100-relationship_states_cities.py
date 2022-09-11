#!/usr/bin/python3
"""
    prints all City objects from the database hbtn_0e_14_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cali = State(name="California")
    cali.cities = [City(name="San Francisco")]
    session.add(cali)
    session.commit()
    session.close()
