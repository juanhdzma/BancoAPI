from fastapi import APIRouter, Depends
from src.application.data.IUser import IUser
from src.application.services.UserService import UserService

banco_router = APIRouter()
userService = UserService()

@banco_router.post("/user")
def createUser(payload: IUser):
    return userService.createUser(payload)

@banco_router.get("/user/{id}")
def getUser(id):
    return userService.getUser(id)

@banco_router.get("/users")
def getUser():
    return userService.getAllUsers()


## Crear Cliente
## Configurar los productos del banco (tipos de cuentras de ahorro y tipos de tarjeta de credito)
## Consulta de saldo (Corrientes, ahorro, credito)
## Historial de transacciones
## Transferencia de fondos entre propias cuentas y otras