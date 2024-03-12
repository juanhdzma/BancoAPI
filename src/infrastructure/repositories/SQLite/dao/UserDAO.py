from src.infrastructure.repositories.SQLite.adapter.SQLiteDatabase import SQLiteDatabase
from src.infrastructure.repositories.SQLite.models.User import User
from src.domain.repository.UserRepository import UserRepository

class UserDAO(UserRepository):
    def __init__(self):
        self.database = SQLiteDatabase()

    def crearUsuario(self, IUserIn):
        try:
            session = self.database.createConnection()
            new_user = User(**IUserIn)
            session.add(new_user)
            session.commit()
            return True
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)

    def consultarUsuario(self, id):
        try:
            session = self.database.createConnection()
            user = session.query(User).filter_by(id=id).first()
            return user
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)

    def consultarUsuarios(self):
        try:
            session = self.database.createConnection()
            users = session.query(User).all()
            return users
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)