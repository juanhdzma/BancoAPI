from fastapi import APIRouter
from src.application.data.IUser import IUser
from src.application.data.IAccount import IAccount
from src.application.services.UserService import UserService
from src.application.services.AccountService import AccountService

banco_router = APIRouter()
userService = UserService()
accountService = AccountService()

@banco_router.post("/user")
def createUser(payload: IUser):
    return userService.createUser(payload)

@banco_router.get("/user/{idUser}")
def getUser(idUser):
    return userService.getUser(idUser)

@banco_router.get("/users")
def getUser():
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

# Hacer consignacion
# Desactivar cuenta


# Mostrar historial de una cuenta
# Transferir de una cuenta a otra


