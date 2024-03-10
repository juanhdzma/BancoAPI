from sqlalchemy import Column, String
from src.infrastructure.repositories.SQLite.models.ModelsCreator import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(String(50), primary_key=True)
    phone = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), unique=False, nullable=False)
    lastName = Column(String(100), unique=False, nullable=False)