from pydantic import BaseModel, field_validator


class IConsignment(BaseModel):
    destination_account: int
    value: float

    @field_validator("destination_account")
    def validateDestinationAccount(cls, value):
        if value > 0:
            return value
        raise ValueError("La cuenta no es valida")

    @field_validator("value")
    def validateValue(cls, value):
        if value > 0:
            return value
        raise ValueError("El valor de consignacion no es valido")
