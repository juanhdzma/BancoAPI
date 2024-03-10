from src.infrastructure.repositories.SQLite.dao.UserDAO import UserDAO

class CreateUserService:
    def __init__(self, IUserIn):
        self.createUser(IUserIn)

    def createUser(self, IUserIn):
        dao = UserDAO()
        response = dao.crearUsuario(IUserIn)
        return response