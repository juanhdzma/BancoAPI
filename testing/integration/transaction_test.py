from integration_settings import BASE_URL
from requests import post, get
from util import resetDB, removeTimestamp, removeTransactionDatetime
from data.account_test_data import CreateAccountIN
from data.user_test_data import CreateUserIN
from data.transaction_test_data import (
    ConsignmentIN, ConsignmentOUT, TransactionOUT, TransactionIN, RecordOUT
)


@resetDB
def test_consignment():
    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)

    noFieldResponse = post(f"{BASE_URL}/consignment", json=ConsignmentIN.noField)
    notFoundResponse = post(f"{BASE_URL}/consignment", json=ConsignmentIN.notFound)
    invalidValueResponse = post(f"{BASE_URL}/consignment", json=ConsignmentIN.invalidValue)

    assert removeTimestamp(noFieldResponse.json()) == ConsignmentOUT.noField, \
        'Error cuando no se envia un campo al realizar consignacion'
    assert removeTimestamp(notFoundResponse.json()) == ConsignmentOUT.notFound, \
        'Error cuando no se encuentra la cuenta al realizar consignacion'
    assert removeTimestamp(invalidValueResponse.json()) == ConsignmentOUT.invalidValue, \
        'Error cuando se envia un valor invalido al realizar consignacion'

    validResponse = post(f"{BASE_URL}/consignment", json=ConsignmentIN.validData)
    assert removeTimestamp(validResponse.json()) == ConsignmentOUT.validResponse, \
        'Error cuando se envia valores validos al realizar consignacion'


@resetDB
def test_transaction():
    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    post(f"{BASE_URL}/consignment", json=ConsignmentIN.validData)

    noFieldResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.noField)
    invalidIDResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.invalidID)
    invalidValueResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.invalidValue)
    notSameResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.notSame)
    noDestinationResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.noDestination)
    noOriginResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.noOrigin)
    noMoneyResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.noMoney)
    validResponse = post(f"{BASE_URL}/transfer", json=TransactionIN.validData)

    assert removeTimestamp(validResponse.json()) == TransactionOUT.validResponse, \
        'Error cuando se manda una transferencia valida'
    assert removeTimestamp(noFieldResponse.json()) == TransactionOUT.noField, \
        'Error cuando no se envia un campo al transferir'
    assert removeTimestamp(invalidIDResponse.json()) == TransactionOUT.invalidID, \
        'Error cuando el ID es invalido al transferir'
    assert removeTimestamp(invalidValueResponse.json()) == TransactionOUT.invalidValue, \
        'Error cuando el valor es invalido al transferir'
    assert removeTimestamp(notSameResponse.json()) == TransactionOUT.notSame, \
        'Error cuando la cuenta origen y destino son las mismas al transferir'
    assert removeTimestamp(noDestinationResponse.json()) == TransactionOUT.noDestination, \
        'Error cuando no existe la cuenta destino al transferir'
    assert removeTimestamp(noOriginResponse.json()) == TransactionOUT.noOrigin, \
        'Error cuando no existe la cuenta origen al transferir'
    assert removeTimestamp(noMoneyResponse.json()) == TransactionOUT.noMoney, \
        'Error cuando no hay fondos para transferir'


@resetDB
def test_get_record():
    post(f"{BASE_URL}/user", json=CreateUserIN.validData1)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    post(f"{BASE_URL}/account", json=CreateAccountIN.validData)
    post(f"{BASE_URL}/consignment", json=ConsignmentIN.validData)
    post(f"{BASE_URL}/transfer", json=TransactionIN.validData)

    validResponse = get(f"{BASE_URL}/record/1")
    invalidIDResponse = get(f"{BASE_URL}/record/a")
    notFoundresponse = get(f"{BASE_URL}/record/100")

    assert removeTransactionDatetime(validResponse.json()) == RecordOUT.validResponse, \
        'Error al obtener historial de transacciones'
    assert removeTimestamp(invalidIDResponse.json()) == RecordOUT.invalidID, \
        'Error al enviar ID invalido al obtener historial de transacciones'
    assert removeTimestamp(notFoundresponse.json()) == RecordOUT.notFound, \
        'Error al no encontrar historial de transacciones'
