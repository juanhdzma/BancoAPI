from pydantic import BaseModel, field_validator


class ITransaction(BaseModel):
    source_account: int
    destination_accout: int
    value: float

    @field_validator("source_account", "destination_accout")
    def validateUserId(cls, value):
        if value > 0:
            return value
        raise ValueError("Las cuentas no son validas")
    
    @field_validator("value")
    def validateUserId(cls, value):
        if value > 0:
            return value
        raise ValueError("El valor de transferencia no es valido")