
class CreateUserIN:
    validData1 = {
        "id": "1",
        "phone": "3187951218",
        "name": "Juan",
        "last_name": "Hernandez"
    }
    validData2 = {
        "id": "2",
        "phone": "1234567890",
        "name": "Daniel",
        "last_name": "Saavedra"
    }
    noField = {
        "phone": "3187951218",
        "name": "Juan",
        "last_name": "Hernandez"
    }
    invalidPhone = {
        "id": "1",
        "phone": "1",
        "name": "Juan",
        "last_name": "Hernandez"
    }
    invalidID = {
        "id": "abc",
        "phone": "3187951218",
        "name": "Juan",
        "last_name": "Hernandez"
    }


class GetUserOUT:
    responseUser1 = {
        "is_error": False,
        "data": {
            "id": "1",
            "phone": "3187951218",
            "name": "Juan",
            "last_name": "Hernandez"
        },
        "status_code": 200
    }
    responseUsers = {
    "is_error": False,
    "data": [
        {
            "id": "1",
            "phone": "3187951218",
            "name": "Juan",
            "last_name": "Hernandez"
        },
        {
            "id": "2",
            "phone": "1234567890",
            "name": "Daniel",
            "last_name": "Saavedra"
        }
    ],
    "status_code": 200
}