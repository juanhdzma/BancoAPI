from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.repositories.SQL.models.ModelsCreator import Base


class CloudDatabase:
    def __init__(self):
        self.engine = create_engine('postgresql://banco:admin1234@banco-api.ch8ia2qyebpp.us-east-2.rds.amazonaws.com:5432/operations')

    def createConnection(self):
        currentSession = sessionmaker(bind=self.engine)
        session = currentSession()
        return session

    def closeConnection(self, session):
        session.close()