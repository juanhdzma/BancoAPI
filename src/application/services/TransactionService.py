from src.application.data.IConsignment import IConsignment
from src.application.data.ITransaction import ITransaction
from src.domain.response.Result import *
from src.domain.response.CustomException import *
from src.domain.response.Response import Response
from src.infrastructure.configuration.DependencyContainer import DependencyContainer
from src.domain.repository.AccountRepository import AccountRepository
from src.domain.repository.UserRepository import UserRepository
from src.domain.repository.TransactionRepository import TransactionRepository
from injector import Injector


class TransactionService:
    def __init__(self):
        self.injector = Injector([DependencyContainer()])
        self.account_service = self.injector.get(AccountRepository)
        self.user_service = self.injector.get(UserRepository)
        self.transaction_service = self.injector.get(TransactionRepository)

    def consignAccount(self, consignment: IConsignment):
        params = consignment.model_dump()
        account = self.account_service.consultarCuenta(params['destination_account'])
        if account:
            result = self.transaction_service.hacerConsignacion(params)
            if result:
                return Response.ok(CorrectResult("Consignacion realizada con exito"))
            return Response.failure(InternalServerErrorException("Error al realizar la consignacion"))
        return Response.failure(BadRequestException("No existe esta cuenta"))

    def getRecords(self, idAccount):
        if idAccount.isdigit():
            result = self.transaction_service.historialTransferencias(idAccount)
        else:
            return Response.failure(BadRequestException("Id no valido"))

        if result:
            result = [i.serialize() for i in result]
            return Response.ok(CorrectResult(result))
        return Response.failure(NotFoundException("No hay transacciones asociadas a esta cuenta"))

    def transferMoney(self, transfer: ITransaction):
        pass
