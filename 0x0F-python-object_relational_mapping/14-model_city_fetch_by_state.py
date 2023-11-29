#!/usr/bin/python3
"""
This is a module documentation for my file
"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        stmt = select(City, State).join(State, City.state_id == State.id)
        for result in session.execute(stmt):
            city_obj = result[0]
            state_obj = result[1]
            print("{}: ({}) {}"
                  .format(state_obj.name, city_obj.id, city_obj.name))
