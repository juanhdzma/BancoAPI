from requests import post, get
from integration_settings import BASE_URL
from data.user_test_data import CreateUserIN, GetUserOUT
from util import resetDB, removeTimestamp

@resetDB
def test_create_user():
    validResponse = post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    noFieldResponse = post(f"{BASE_URL}/user", json=CreateUserIN.noField)
    invalidIDResponse = post(f"{BASE_URL}/user", json=CreateUserIN.invalidID)
    invalidPhoneResponse = post(f"{BASE_URL}/user", json=CreateUserIN.invalidPhone)
    repeatedResponse = post(f"{BASE_URL}/user", json=CreateUserIN.validData1)

    assert validResponse.status_code == 201, 'Error en datos validos al crear usuario'
    assert noFieldResponse.status_code == 400, 'Error en campo no enviado al crear usuario'
    assert invalidIDResponse.status_code == 400, 'Error en cedula invalida al crear usuario'
    assert invalidPhoneResponse.status_code == 400, 'Error en telefono invalido al crear usuario'
    assert repeatedResponse.status_code == 409, 'Error en usuario repetido al crear usuario'

@resetDB
def test_get_user():
    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)

    validResponse = get(f"{BASE_URL}/user/1")
    invalidIDResponse = get(f"{BASE_URL}/user/a")
    notFoundResponse = get(f"{BASE_URL}/user/2")

    assert validResponse.status_code == 200, 'Error al validar el codigo de respuesta cuando se obtiene un usuario valido'
    assert removeTimestamp(validResponse.json) == GetUserOUT.responseUser1, 'Error al validar data cuando se obtiene un usuario valido'

    assert invalidIDResponse.status_code == 400, 'Error en ID invalido al obtener usuario'
    assert notFoundResponse.status_code == 404, 'Error en usuario no encontrado al obtener usuario'

@resetDB
def test_get_users():
    notFoundResponse = get(f"{BASE_URL}/users")
    assert notFoundResponse.status_code == 404, 'Error cuando no hay usuarios al obtener los usuarios'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/user", json=CreateUserIN.validData2)
    validResponse = get(f"{BASE_URL}/users")

    assert validResponse.status_code == 200, 'Error al validar el codigo de respuesta cuando se obtienen los usuarios'
    assert removeTimestamp(validResponse.json) == GetUserOUT.responseUsers, 'Error al validar data cuando se obtienen los usuarios'
