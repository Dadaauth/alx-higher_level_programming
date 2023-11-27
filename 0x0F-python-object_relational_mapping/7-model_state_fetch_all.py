#!/usr/bin/python3
"""
This is a module documentation for my file
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State).order_by(State.id)
        for result in session.scalars(stmt):
            print("{}: {}".format(result.id, result.name))
    Base.metadata.create_all(engine)
