from pydantic import BaseModel, field_validator


class ITransaction(BaseModel):
    source_account: int
    destination_account: int
    value: float

    @field_validator("source_account", "destination_account")
    def validateAccount(cls, value):
        if value > 0:
            return value
        raise ValueError("Las cuentas no son validas")
    
    @field_validator("value")
    def validateValue(cls, value):
        if value > 0:
            return value
        raise ValueError("El valor de transferencia no es valido")