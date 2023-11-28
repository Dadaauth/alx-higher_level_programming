#!/usr/bin/python3
"""
This is a module documentation for my file
"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
# from model_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # ~~~ SAME RESULT WITH CODE BELOW
    with Session() as session:
        stmt = select(State)
        for result in session.scalars(stmt):
            for city in result.cities:
                print("{}: ({}) {}".format(result.name, city.id, city.name))
    # ~~~ SAME RESULT WITH CODE BELOW

    # OR USE THE CODE BELOW ==> SAME RESULT

    # with Session() as session:
    #     stmt = select(City).join(State).order_by(City.id)
    #     for result in session.scalars(stmt):
    #         print("{}: ({}) {}".format(result.states.name, result.id, result.name))
