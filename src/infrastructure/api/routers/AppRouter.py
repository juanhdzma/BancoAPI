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


# Configurar los productos del banco (tipos de cuentras de ahorro y tipos de tarjeta de credito)
# Consulta de saldo (Corrientes, ahorro, credito)
# Historial de transacciones
# Transferencia de fondos entre propias cuentas y otras