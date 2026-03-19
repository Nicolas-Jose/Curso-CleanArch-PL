from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import base

class Users(base):
    __tablename__ = "users"

    id = Column[int](Integer, primary_key=True, autoincrement=True)
    first_name = Column[str](String, nullable=False)
    last_name = Column[str](String, nullable=False)
    age = Column[int](Integer, nullable=False)

    def __repr__(self):
        return f"Users [id={self.id}, firt_name={self.first_name}]"