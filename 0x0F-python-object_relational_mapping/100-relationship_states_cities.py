#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database
Usage: ./100-relationship_states_cities.py <mysql username> /
                                           <mysql password> /
                                           <database name>
Session
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        newCity = City(name="San Francisco")
        newState = State(name="California", cities=[newCity])
        Base.metadata.create_all(engine)
        session.add(newState)
        session.commit()
