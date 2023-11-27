#!/usr/bin/python3
"""
This is a module documentation for my file
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class State(Base):
    """
    Documentaion for State class
    """
    __tablename__= "states"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

