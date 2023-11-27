#!/usr/bin/python3
"""
My module documentation
"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    new_name = "New Mexico"

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    with Session() as session:
        stmt = select(State).where(State.id == 2)
        result = session.scalar(stmt)
        result.name = new_name
        session.commit()
