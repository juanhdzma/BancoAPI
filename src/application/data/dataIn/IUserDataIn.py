from pydantic import BaseModel, validator

class IUserIn(BaseModel):
    id: str
    phone: str
    name: str
    lastName: str

    @validator("id")
    def validateCedula(cls, value):
        if value.isdigit():
            return value
        raise ValueError("La cedula no es valida")
    
    @validator("phone")
    def validateCedula(cls, value):
        if value.isdigit() and len(value) == 10:
            return value
        raise ValueError("El telefono no es valido")
    
    @validator("name", "lastName")
    def validateCedula(cls, value):
        if value.isalpha():
            return value
        raise ValueError("El nombre o apellido no son validos")