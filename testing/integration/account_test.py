from integration_settings import BASE_URL
from requests import post, get
from data.account_test_data import CreateAccountIN, CreateAccountOUT, GetAccountOUT
from data.user_test_data import CreateUserIN
from util import resetDB, removeTimestamp

@resetDB
def test_create_account():
    notFoundResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.notFoundData)
    invalidAccountTypeResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.invalidAccounTypeData)
    noFieldResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.noFieldData)

    assert removeTimestamp(notFoundResponse.json()) == CreateAccountOUT.notFoundData, 'Error cuando no hay usuarios para crear la cuenta'
    assert removeTimestamp(invalidAccountTypeResponse.json()) == CreateAccountOUT.invalidAccounTypeData, 'Error cuando el tipo de cuenta es invalido al crearla'
    assert removeTimestamp(noFieldResponse.json()) == CreateAccountOUT.noFieldData, 'Error cuando no se envia un campo al crear una cuenta'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    validResponse = post(f"{BASE_URL}/account", json=CreateAccountIN.validData)

    assert removeTimestamp(validResponse.json()) == CreateAccountOUT.validData, 'Error cuando se crea una cuenta valida'


@resetDB
def test_get_account():
    invalidIDResponse = get(f"{BASE_URL}/account/a")
    notFoundResponse = get(f"{BASE_URL}/account/100")

    assert removeTimestamp(invalidIDResponse.json()) == GetAccountOUT.invalidIDResponse, 'Error cuando el tipo de cuenta es invalido al crearla'
    assert removeTimestamp(notFoundResponse.json()) == GetAccountOUT.notFoundResponse, 'Error cuando no se envia un campo al crear una cuenta'

    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    validResponse = get(f"{BASE_URL}/account/1")

    assert removeTimestamp(validResponse.json()) == GetAccountOUT.validResponse, 'Error cuando no hay usuarios para crear la cuenta'



# def test_get_accounts():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'

# def test_deactivate_account():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'