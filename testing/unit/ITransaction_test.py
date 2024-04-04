from pytest import raises
from src.application.data.ITransaction import ITransaction
from data.ITransaction_test_data import ITransactionCases


def test_valid_input():
    account = ITransaction(**ITransactionCases.validData)
    assert account.source_account == ITransactionCases.validData["source_account"], \
        'Error al obtener ID cuenta origen de una validacion correcta'
    assert account.destination_account == ITransactionCases.validData["destination_account"], \
        'Error al obtener ID cuenta destino de una validacion correcta'
    assert account.value == ITransactionCases.validData["value"], \
        'Error al obtener valor de una validacion correcta'


def test_invalid_destinationAccount():
    with raises(ValueError) as excinfo:
        ITransaction(**ITransactionCases.invalidDestination)
    assert excinfo.value.errors()[0]['msg'] == \
        "Input should be a valid integer, unable to parse string as an integer", \
        'Error al validar cuenta destino invalida'


def test_invalid_sourceAccount():
    with raises(ValueError) as excinfo:
        ITransaction(**ITransactionCases.invalidSource)
    assert excinfo.value.errors()[0]['msg'] == \
        "Input should be a valid integer, unable to parse string as an integer", \
        'Error al validar cuenta origen invalida'


def test_invalid_value():
    with raises(ValueError) as excinfo:
        ITransaction(**ITransactionCases.invalidValue)
    assert excinfo.value.errors()[0]['msg'] == \
        "Value error, El valor de transferencia no es valido", \
        'Error al validar valor de consignacion invalido'
