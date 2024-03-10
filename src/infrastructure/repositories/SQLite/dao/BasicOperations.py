from src.infrastructure.repositories.SQLite.adapter.SQLiteDatabase import SQLiteDatabase
from src.infrastructure.repositories.SQLite.models.User import User
from src.domain.response.Exceptions import *
from src.domain.response.Result import *

class BasicOperations:
    def __init__(self):
        self.database = SQLiteDatabase()

    def add_user(self, username, email):
        session = self.database.createConnection()
        try:
            new_user = User(username=username, email=email)
            session.add(new_user)
            session.commit()
            return Result.ok("Terminado")
        except BaseException:
             return Result.failure(BadMessageException("Fallo en repetido", "Volver a intentar"))
        finally:
            self.database.closeConnection(session)

    def get_all_users(self):
        session = self.database.createConnection()
        all_users = session.query(User).all()
        self.database.closeConnection(session)
        return all_users