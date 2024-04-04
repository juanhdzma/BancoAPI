class CreateAccountIN:
    validData = {
        "user_id": "1",
        "account_type": "Corriente"
    }
    notFoundData = {
        "user_id": "100",
        "account_type": "Ahorros"
    }
    invalidAccounTypeData = {
        "user_id": "1",
        "account_type": "A la mano"
    }
    noFieldData = {
        "account_type": "A la mano"
    }


class CreateAccountOUT:
    validData = {
        "is_error": False,
        "data": "Cuenta creada correctamente",
        "status_code": 201
    }
    notFoundData = {
        "is_error": True,
        "message": "El usuario no existe en la base de datos",
        "status_code": 400
    }
    invalidAccounTypeData = {
        "is_error": True,
        "message": "Value error, El tipo de cuenta no es valida",
        "status_code": 400
    }
    noFieldData = {
        "is_error": True,
        "message": "Field required",
        "status_code": 400
    }


class GetAccountOUT:
    validResponse = {
        "is_error": False,
        "data": {
            "id": 1,
            "user_id": "1",
            "account_type": "Corriente",
            "balance": 0,
            "status": True
        },
        "status_code": 200
    }
    invalidIDResponse = {
        "is_error": True,
        "message": "Id no valido",
        "status_code": 400
    }
    notFoundResponse = {
        "is_error": True,
        "message": "La cuenta no esta registrada en la base de datos",
        "status_code": 404
    }


class GetAccountsOUT:
    invalidIDResponse = {
        "is_error": True,
        "message": "Id no valido",
        "status_code": 400
    }
    notFoundResponse = {
        "is_error": True,
        "message": "No hay cuentas asignadas a este id",
        "status_code": 404
    }
    validResponse = {
        "is_error": False,
        "data": [
            {
                "id": 1,
                "user_id": "1",
                "account_type": "Corriente",
                "balance": 0.0,
                "status": True
            },
            {
                "id": 2,
                "user_id": "1",
                "account_type": "Corriente",
                "balance": 0.0,
                "status": True
            }
        ],
        "status_code": 200
    }


class DeactivateAccountOUT:
    validResponse = {
        "is_error": False,
        "data": "La cuenta ha sido desactivada, el saldo a desembolsar es $0.0",
        "status_code": 200
    }
    invalidID = {
        "is_error": True,
        "message": "Id no valido",
        "status_code": 400
    }
    notFound = {
        "is_error": True,
        "message": "La cuenta no esta registrada en la base de datos",
        "status_code": 404
    }
