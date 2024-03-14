from src.domain.response.Result import *
from src.domain.response.CustomException import *
from src.domain.response.Response import Response
from src.infrastructure.configuration.DependencyContainer import DependencyContainer
from src.domain.repository.AccountRepository import AccountRepository
from src.domain.repository.UserRepository import UserRepository
from injector import Injector


class AccountService:
    def __init__(self):
        self.injector = Injector([DependencyContainer()])
        self.account_service = self.injector.get(AccountRepository)
        self.user_service = self.injector.get(UserRepository)
    
    def createAccount(self, params):
        params = params.model_dump()
        existeUsuario = self.user_service.consultarUsuario(params['user_id'])
        if existeUsuario:
            result = self.account_service.crearCuenta(params)
            if result:
                return Response.ok(EntityCreated("Cuenta creada correctamente"))
            return Response.failure(InternalServerErrorException("Error al crear la cuenta del usuario"))
        else:
            return Response.failure(BadRequestException("El usuario no existe en la base de datos"))
    
    def getAccount(self, idAccount):
        if idAccount.isdigit():
            result = self.account_service.consultarCuenta(idAccount)
        else:
            return Response.failure(BadRequestException("Id no valido"))

        if result:
            result = result.serialize()
            return Response.ok(CorrectResult(result))
        return Response.failure(NotFoundException("La cuenta no esta registrada en la base de datos"))
    
    def getAllUserAccounts(self, idUser):
        if idUser.isdigit():
            result = self.account_service.consultarCuentas(idUser)
        else:
            return Response.failure(BadRequestException("Id no valido"))

        if result:
            result = [i.serialize() for i in result]
            return Response.ok(CorrectResult(result))
        return Response.failure(NotFoundException("No hay cuentas asignadas a este id"))