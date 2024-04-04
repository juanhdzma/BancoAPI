from integration_settings import BASE_URL
from requests import post, get, delete
from data.account_test_data import (
    CreateAccountIN, CreateAccountOUT, GetAccountOUT, GetAccountsOUT, DeactivateAccountOUT
)
from data.user_test_data import CreateUserIN
from util import resetDB, removeTimestamp


@resetDB
def test_create_account():
    notFoundResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.notFoundData)
    invalidAccountTypeResponse = post(f"{BASE_URL}/account",
                                      json=CreateAccountIN.invalidAccounTypeData)
    noFieldResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.noFieldData)

    assert removeTimestamp(notFoundResponse.json()) == CreateAccountOUT.notFoundData, \
        'Error cuando no hay usuarios para crear la cuenta'
    assert removeTimestamp(invalidAccountTypeResponse.json()) == \
        CreateAccountOUT.invalidAccounTypeData, \
        'Error cuando el tipo de cuenta es invalido al crearla'
    assert removeTimestamp(noFieldResponse.json()) == CreateAccountOUT.noFieldData, \
        'Error cuando no se envia un campo al crear una cuenta'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    validResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.validData)

    assert removeTimestamp(validResponse.json()) == CreateAccountOUT.validData, \
        'Error cuando se crea una cuenta valida'


@resetDB
def test_get_account():
    invalidIDResponse = get(f"{BASE_URL}/account/a")
    notFoundResponse = get(f"{BASE_URL}/account/100")

    assert removeTimestamp(invalidIDResponse.json()) == GetAccountOUT.invalidIDResponse, \
        'Error cuando el tipo de cuenta es invalido al obtener la cuenta'
    assert removeTimestamp(notFoundResponse.json()) == GetAccountOUT.notFoundResponse, \
        'Error cuando no hay una cuenta con es ID'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    validResponse = get(f"{BASE_URL}/account/1")

    assert removeTimestamp(validResponse.json()) == GetAccountOUT.validResponse, \
        'Error cuando se obtiene un cuenta valida'


@resetDB
def test_get_accounts():
    invalidIDResponse = get(f"{BASE_URL}/accounts/a")
    notFoundResponse = get(f"{BASE_URL}/accounts/100")

    assert removeTimestamp(invalidIDResponse.json()) == GetAccountsOUT.invalidIDResponse, \
        'Error cuando el ID es invalido al obtener las cuentas'
    assert removeTimestamp(notFoundResponse.json()) == GetAccountsOUT.notFoundResponse, \
        'Error cuando no hay cuentas asignadas a este ID'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    validResponse = get(f"{BASE_URL}/accounts/1")

    assert removeTimestamp(validResponse.json()) == GetAccountsOUT.validResponse, \
        'Error cuando se obtienen las cuentas de un ID valido'


@resetDB
def test_deactivate_account():
    invalidIDResponse = delete(f"{BASE_URL}/account/a")
    notFoundResponse = delete(f"{BASE_URL}/account/100")
    assert removeTimestamp(invalidIDResponse.json()) == DeactivateAccountOUT.invalidID, \
        'Error cuando el ID es invalido al desactivar una cuenta'
    assert removeTimestamp(notFoundResponse.json()) == DeactivateAccountOUT.notFound, \
        'Error al no encontrar la cuenta al desactivar una cuenta'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)

    validResponse = delete(f"{BASE_URL}/account/1")
    assert removeTimestamp(validResponse.json()) == DeactivateAccountOUT.validResponse, \
        'Error al desactivar una cuenta valida'

    alreadyDeleted = delete(f"{BASE_URL}/account/1")
    assert removeTimestamp(alreadyDeleted.json()) == DeactivateAccountOUT.notFound, \
        'Error al desactivar una cuenta que ya fue desactivada'
