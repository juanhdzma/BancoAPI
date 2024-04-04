from pydantic import BaseModel, field_validator

validAccountTypes = ['Ahorros', 'Corriente', 'Tarjeta de Credito']


class IAccount(BaseModel):
    user_id: str
    account_type: str

    @field_validator("user_id")
    def validateUserId(cls, value):
        if value.isdigit():
            return value
        raise ValueError("La cedula no es valida")

    @field_validator("account_type")
    def validateAccountType(cls, value):
        if value in validAccountTypes:
            return value
        raise ValueError("El tipo de cuenta no es valida")
