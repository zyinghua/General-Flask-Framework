from sqlalchemy import Integer, Column, String, DateTime, DECIMAL, Float
from database import Base
from dataclasses import dataclass


@dataclass
class User(Base):
    """An example of declaring a class -> table using ORM (Object Relational Mapping)."""
    __tablename__ = 'User'
    user_id: int
    user_name: str
    user_email: str

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    user_email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.user_name = name
        self.user_email = email

    def __repr__(self):
        return f'<User {self.user_name!r}>'
