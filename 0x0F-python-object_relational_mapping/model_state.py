#!/usr/bin/python3
"""
This is a module documentation for my file
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from model_city import Base


class State(Base):
    """
    Documentation for State class
    """
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
