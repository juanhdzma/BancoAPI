from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.repositories.SQLite.models.ModelsCreator import Base

class SQLiteDatabase():
    def __init__(self):
        self.engine = self.__initializeDatabase()
        self.__createTables()

    def __initializeDatabase(self):
        return create_engine('sqlite:///operaciones.db')
    
    def __createTables(self):
        Base.metadata.create_all(self.engine)

    def createConnection(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def closeConnection(self, session):
        session.close()