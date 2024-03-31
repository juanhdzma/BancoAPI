from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.Envs import DB_NAME
from src.infrastructure.repository.SQL.model.ModelsCreator import Base


class SQLiteDatabase:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{DB_NAME}.db')
        self.__createTables()

    def __createTables(self):
        Base.metadata.create_all(self.engine)

    def createConnection(self):
        currentSession = sessionmaker(bind=self.engine)
        session = currentSession()
        return session

    def closeConnection(self, session):
        session.close()
