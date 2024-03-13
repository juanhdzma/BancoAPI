from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.repositories.SQL.models.ModelsCreator import Base


class SQLiteDatabase:
    def __init__(self):
        self.engine = create_engine('sqlite:///operaciones.db')
        self.__createTables()

    def __createTables(self):
        Base.metadata.create_all(self.engine)

    def createConnection(self):
        currentSession = sessionmaker(bind=self.engine)
        session = currentSession()
        return session

    def closeConnection(self, session):
        session.close()
