from src.infrastructure.repositories.SQLite.adapter.SQLiteDatabase import SQLiteDatabase
from src.infrastructure.repositories.SQLite.models.User import User
from src.domain.response.Exceptions import *
from src.domain.response.Response import *

class BasicOperations:
    def __init__(self):
        self.database = SQLiteDatabase()

    def add_user(self, username, email):
        session = self.database.createConnection()
        try:
            new_user = User(username=username, email=email)
            session.add(new_user)
            session.commit()
            return Response.ok("Terminado", StatusCode.CREATED)
        except BaseException:
            return Response.failure(BadMessageException("Fallo en repetido"))
        finally:
            self.database.closeConnection(session)

    def get_all_users(self):
        session = self.database.createConnection()
        all_users = session.query(User).all()
        self.database.closeConnection(session)
        return all_users