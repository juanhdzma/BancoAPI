from pydantic import BaseModel, field_validator


class IConsignment(BaseModel):
    destination_accout: int
    value: float

    @field_validator("destination_accout")
    def validateUserId(cls, value):
        if value > 0:
            return value
        raise ValueError("La cuenta no es valida")
    
    @field_validator("value")
    def validateUserId(cls, value):
        if value > 0:
            return value
        raise ValueError("El valor de consignacion no es valido")