from sqlalchemy import Column, String, Integer, Float
from src.infrastructure.repositories.SQL.models.ModelsCreator import Base
from dataclasses import dataclass


@dataclass
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(50), unique=False, nullable=False)
    account_type = Column(String(20), unique=False, nullable=False)
    balance = Column(Float, unique=False, nullable=False, default=0.0)

    def serialize(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
