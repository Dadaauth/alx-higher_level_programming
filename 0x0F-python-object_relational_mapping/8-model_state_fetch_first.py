#!/usr/bin/python3
"""
This is a module documentation for my file
"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State)
        result = session.scalars(stmt).first()
        # OR USE result = session.scalar(stmt)
        if result is not None:
            print("{}: {}".format(result.id, result.name))
        else:
            print("Nothing")
    Base.metadata.create_all(engine)
