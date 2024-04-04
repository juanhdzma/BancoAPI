from pytest import raises
from src.application.data.IConsignment import IConsignment
from data.IConsignment_test_data import IConsignmentCases


def test_valid_input():
    account = IConsignment(**IConsignmentCases.validData)
    assert account.destination_account == IConsignmentCases.validData["destination_account"], \
        'Error al obtener ID cuenta de una validacion correcta'
    assert account.value == IConsignmentCases.validData["value"], \
        'Error al obtener valor de una validacion correcta'


def test_invalid_destinationAccount():
    with raises(ValueError) as excinfo:
        IConsignment(**IConsignmentCases.invalidDestination)
    assert excinfo.value.errors()[0]['msg'] == \
        "Input should be a valid integer, unable to parse string as an integer", \
        'Error al validar cuenta invalida'


def test_invalid_value():
    with raises(ValueError) as excinfo:
        IConsignment(**IConsignmentCases.invalidValue)
    assert excinfo.value.errors()[0]['msg'] == \
        "Value error, El valor de consignacion no es valido", \
        'Error al validar valor de consignacion invalido'
