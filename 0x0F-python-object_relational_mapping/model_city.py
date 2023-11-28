#!/usr/bin/python3
"""
This is a module documentation for my file
"""

from model_state import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey


class City(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True,
                                    nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"),
                                          nullable=False)
    # OR USE state_id = mapped_column(ForeignKey("states.id"), nullable=False)
