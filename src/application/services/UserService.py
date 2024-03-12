from src.domain.response.Result import *
from src.domain.response.Exceptions import *
from src.domain.response.Response import Response
from src.configuration.DependencyContainer import DependencyContainer
from src.domain.repository.UserRepository import UserRepository
from injector import Injector
from fastapi.encoders import jsonable_encoder

class UserService:
    def __init__(self):
        self.injector = Injector([DependencyContainer()])
        self.user_service = self.injector.get(UserRepository)
    
    def createUser(self, params):
        params = params.model_dump()
        result = self.user_service.crearUsuario(params)
        if result == True:
            return Response.ok(EntityCreated("Usuario agregado correctamente"))
        return Response.failure(ConflictException("El usuario ya existe en la base de datos"))
    
    def getUser(self, id):
        result = self.user_service.consultarUsuario(id)
        print(result.serialize())
        if result:
            return Response.ok(EntityCreated("Usuario agregado correctamente"))
        return Response.failure(ConflictException("El usuario ya existe en la base de datos"))
    
    def getAllUsers(self):
        result = self.user_service.consultarUsuarios()
        if result:
            return Response.ok(EntityCreated("Usuario agregado correctamente"))
        return Response.failure(ConflictException("El usuario ya existe en la base de datos"))