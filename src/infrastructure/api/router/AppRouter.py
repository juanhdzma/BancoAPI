from fastapi import APIRouter
from src.application.data.IConsignment import IConsignment
from src.application.data.ITransaction import ITransaction
from src.application.data.IUser import IUser
from src.application.data.IAccount import IAccount
from src.application.service.UserService import UserService
from src.application.service.AccountService import AccountService
from src.application.service.TransactionService import TransactionService

banco_router = APIRouter()
userService = UserService()
accountService = AccountService()
transactionService = TransactionService()

@banco_router.post("/user")
def createUser(payload: IUser):
    return userService.createUser(payload)

@banco_router.get("/user/{idUser}")
def getUser(idUser):
    return userService.getUser(idUser)

@banco_router.get("/users")
def getUsers():
    return userService.getAllUsers()

@banco_router.post("/account")
def createAccount(payload: IAccount):
    return accountService.createAccount(payload)

@banco_router.get("/account/{idAccount}")
def getAccount(idAccount):
    return accountService.getAccount(idAccount)

@banco_router.get("/accounts/{idUser}")
def getUserAccounts(idUser):
    return accountService.getAllUserAccounts(idUser)

@banco_router.delete("/account/{idAccount}")
def deactivateAccount(idAccount):
    return accountService.deactivateAccount(idAccount)

# Hacer consignacion
@banco_router.post("/consignment")
def consignAccount(consignment: IConsignment):
    return transactionService.consignAccount(consignment)

# Mostrar historial de una cuenta
@banco_router.get("/record/{idAccount}")
def getRecords(idAccount):
    return transactionService.getRecords(idAccount)

# Transferir de una cuenta a otra
@banco_router.post("/transfer")
def transferMoney(transfer: ITransaction):
    return transactionService.transferMoney(transfer)


