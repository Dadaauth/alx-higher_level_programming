#!/usr/bin/python3
"""
This is a documentation for my module
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    new_state_name = "Louisiana"

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        new_state = State(name=new_state_name)
        session.add(new_state)
        session.commit()
        print(new_state.id)
