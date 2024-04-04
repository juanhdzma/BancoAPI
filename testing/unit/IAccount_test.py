from pytest import raises
from src.application.data.IAccount import IAccount
from data.IAccount_test_data import IAccountCases


def test_valid_input():
    account = IAccount(**IAccountCases.validData)
    assert account.user_id == IAccountCases.validData["user_id"], 'Error al obtener ID de una validacion correcta'
    assert account.account_type == IAccountCases.validData["account_type"], 'Error al obtener tipo de cuenta de una validacion correcta'


def test_invalid_user_id():
    with raises(ValueError) as excinfo:
        IAccount(**IAccountCases.invalidUserID)
    assert excinfo.value.errors()[0]['msg'] == "Value error, La cedula no es valida", 'Error al validar ID invalido'


def test_invalid_account_type():
    with raises(ValueError) as excinfo:
        IAccount(**IAccountCases.invalidType)
    assert excinfo.value.errors()[0]['msg'] == "Value error, El tipo de cuenta no es valida", 'Error al validar cuenta invalida'
