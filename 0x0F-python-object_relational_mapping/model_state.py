#!/usr/bin/python3
"""
    Python file that contains the class
    definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State Class"""

    __tablename__ = 'states'
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
        )
    name = Column(String(128), nullable=False)