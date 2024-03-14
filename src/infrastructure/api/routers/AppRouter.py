from fastapi import APIRouter
from src.application.data.IUser import IUser
from src.application.services.UserService import UserService

banco_router = APIRouter()
userService = UserService()


@banco_router.post("/user")
def createUser(payload: IUser):
    return userService.createUser(payload)


@banco_router.get("/user/{idUser}")
def getUser(idUser):
    return userService.getUser(idUser)


@banco_router.get("/users")
def getUser():
    return userService.getAllUsers()

# @banco_router.post("/account")
# def createAccount(payload: IUser):
#     return userService.createUser(payload)

# Hacer consignacion

# Crear cuenta
# Desactivar cuenta

# Mostrar historial de una cuenta

# Transferir de una cuenta a otra

# Consultar saldo de todas las cuentas
# Consultar saldo de una cuenta en especifico
