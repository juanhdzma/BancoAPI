from src.infrastructure.repositories.SQLite.adapter.SQLiteDatabase import SQLiteDatabase
from src.infrastructure.repositories.SQLite.models.User import User
from src.domain.response.Exceptions import *
from src.domain.response.Response import *
from src.domain.repository.UserRepository import UserRepository

class UserDAO(UserRepository):
    def __init__(self):
        self.database = SQLiteDatabase()

    def crearUsuario(self, IUserIn):
        session = self.database.createConnection()
        try:
            new_user = User(**IUserIn)
            session.add(new_user)
            session.commit()
            return Response.ok(EntityCreated("Usuario agregado correctamente"))
        except BaseException:
            return Response.failure(BadMessageException("El usuario ya existe en la base de datos"))
        finally:
            self.database.closeConnection(session)

    def consultarUsuario(self, id):
        session = self.database.createConnection()
        try:
            user = session.query(User).filter_by(id=id).first()
            if user:
                return Response.ok(CorrectResult(user))
            return Response.ok(NoContent("Usuario no encontrado"))
        except BaseException:
            return Response.failure(InternalServerErrorException("Fallo en la consulta a realizar"))
        finally:
            self.database.closeConnection(session)