from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.Envs import *


class CloudDatabase:
    def __init__(self):
        self.connection_params = {
            "user": DB_USER,
            "password": DB_PASS,
            "host": DB_HOST,
            "port": DB_PORT,
            "database": DB_NAME
        }
        self.engine = create_engine("postgresql://", connect_args=self.connection_params)

    def createConnection(self):
        currentSession = sessionmaker(bind=self.engine)
        session = currentSession()
        return session

    def closeConnection(self, session):
        session.close()