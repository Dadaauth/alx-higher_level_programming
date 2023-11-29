#!/usr/bin/python3
"""This is a module documentation for my file
I have a documentation but my file ain't long
enough to give m enough information to document anything
so CHECKER!!! please just work Am STRESSED@!! OUT
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    Documentation for State class
    """
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities = relationship("City", back_ref="state", cascade="all, delete-orphan")
