from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql import func
from src.infrastructure.repositories.SQL.model.ModelsCreator import Base
from dataclasses import dataclass


@dataclass
class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source_account = Column(Integer, unique=False, nullable=True)
    destination_account = Column(Integer, unique=False, nullable=False)
    value = Column(Float, unique=False, nullable=False)
    transaction_datetime = Column(DateTime, unique=False, nullable=False, default=func.now())

    def serialize(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
