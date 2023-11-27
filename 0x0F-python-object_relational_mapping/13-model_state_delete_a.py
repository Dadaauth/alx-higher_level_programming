#!/usr/bin/python3

"""
This is my module documentation
"""

import sys
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        stmt = select(State).where(text("BINARY name LIKE '%a%'"))
        for result in session.scalars(stmt):
            print(result.name)
            session.delete(result)
        session.commit()
