from fastapi import APIRouter
from src.infrastructure.repositories.SQLite.dao.BasicOperations import BasicOperations
from src.infrastructure.repositories.SQLite.dao.BasicOperations import BasicOperations

banco_router = APIRouter()

@banco_router.get("/")
def health_checker():
    # Create the UserDao instance
    user_dao = BasicOperations()

    # Add a new user
    respuesta = user_dao.add_user(username='ASdasdasdasd', email='asdasdasdasdsfsdgsdf@example.com')

    # Retrieve all users
    all_users = user_dao.get_all_users()
    for user in all_users:
        print(f"User: {user.username}, Email: {user.email}")

    return respuesta

@banco_router.post("/user")
def createUser():



## Crear Cliente
## Configurar los productos del banco (tipos de cuentras de ahorro y tipos de tarjeta de credito)
## Consulta de saldo (Corrientes, ahorro, credito)
## Historial de transacciones
## Transferencia de fondos entre propias cuentas y otras