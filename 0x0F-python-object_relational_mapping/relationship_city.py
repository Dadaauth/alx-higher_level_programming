#!/usr/bin/python3
"""
This is a module documentation for my file
Documentation for this module is written right here
WHat exactly Do you want from us> Am really stressed out now!!!!!!
"""

from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import String, ForeignKey

Base = declarative_base()


class City(Base):
    """My city class representing the cities table in the mysql DataBase
    his is who dude do you know how to go
    to the museum happy things
    """
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True,
                                    nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"),
                                          nullable=False)
    # OR USE state_id = mapped_column(ForeignKey("states.id"), nullable=False)
