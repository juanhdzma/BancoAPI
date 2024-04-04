class ConsignmentIN:
    validData = {
        "destination_account": "1",
        "value": 10
    }
    noField = {
        "value": 10
    }
    notFound = {
        "destination_account": "10000",
        "value": 10
    }
    invalidValue = {
        "destination_account": "1",
        "value": -1
    }


class ConsignmentOUT:
    validResponse = {
        "is_error": False,
        "data": "Consignacion realizada con exito",
        "status_code": 200
    }
    noField = {
        "is_error": True,
        "message": "Field required",
        "status_code": 400
    }
    notFound = {
        "is_error": True,
        "message": "No existe esta cuenta",
        "status_code": 400
    }
    invalidValue = {
        "is_error": True,
        "message": "Value error, El valor de consignacion no es valido",
        "status_code": 400
    }


class TransactionOUT:
    validResponse = {
        "is_error": False,
        "data": "Transferencia realizada con exito",
        "status_code": 200
    }
    noField = {
        "is_error": True,
        "message": "Field required",
        "status_code": 400
    }
    invalidID = {
        "is_error": True,
        "message": "Input should be a valid integer, unable to parse string as an integer",
        "status_code": 400
    }
    invalidValue = {
        "is_error": True,
        "message": "Value error, El valor de transferencia no es valido",
        "status_code": 400
    }
    notSame = {
        "is_error": True,
        "message": "La cuenta de origen y destino no pueden ser las mismas",
        "status_code": 400
    }
    noDestination = {
        "is_error": True,
        "message": "La cuenta de destino no existe",
        "status_code": 400
    }
    noOrigin = {
        "is_error": True,
        "message": "La cuenta de origen no existe",
        "status_code": 400
    }
    noMoney = {
        "is_error": True,
        "message": "Saldo insuficiente para transferir",
        "status_code": 400
    }


class TransactionIN:
    validData = {
        "source_account": "1",
        "destination_account": "2",
        "value": 10
    }
    noField = {
        "destination_account": "1",
        "value": 10
    }
    invalidID = {
        "source_account": "a",
        "destination_account": "1",
        "value": 10
    }
    invalidValue = {
        "source_account": "1",
        "destination_account": "2",
        "value": -10
    }
    notSame = {
        "source_account": "1",
        "destination_account": "1",
        "value": 10
    }
    noDestination = {
        "source_account": "1",
        "destination_account": "100",
        "value": 10
    }
    noOrigin = {
        "source_account": "100",
        "destination_account": "1",
        "value": 10
    }
    noMoney = {
        "source_account": "2",
        "destination_account": "1",
        "value": 10
    }


class RecordOUT:
    notFound = {
        "is_error": True,
        "message": "No hay transacciones asociadas a esta cuenta",
        "status_code": 404
    }
    invalidID = {
        "is_error": True,
        "message": "Id no valido",
        "status_code": 400
    }
    validResponse = {
        "is_error": False,
        "data": [
            {
                "id": 1,
                "source_account": None,
                "destination_account": 1,
                "value": 10.0
            },
            {
                "id": 2,
                "source_account": 1,
                "destination_account": 2,
                "value": 10.0
            }
        ],
        "status_code": 200
    }
