#!/usr/bin/python3
"""
Documentation for this module
"""

import sys
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])
                           , pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        stmt = select(State).where(text("name = :state_name"))
        result = session.scalar(stmt, {"state_name": sys.argv[4]})
        if result is None:
            print("Not found")
        else:
            print(result.id)
