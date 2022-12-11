"""Define your database structure here..."""

from sqlalchemy import Integer, Column, String, DateTime, DECIMAL, Float
from database import Base
from dataclasses import dataclass


@dataclass  # Use of dataclass: https://stackoverflow.com/a/47955313/17454629
class User(Base):
    """An example of declaring a class -> table using ORM (Object Relational Mapping)."""
    __tablename__ = 'User'
    user_id: int
    user_name: str
    user_email: str

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    user_email = Column(String(120), unique=True)
