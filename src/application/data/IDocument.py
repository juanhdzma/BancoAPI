from pydantic import BaseModel, validator

class IDocument(BaseModel):
    id: str

    @validator("id")
    def validateId(cls, value):
        if value.isdigit():
            return value
        raise ValueError("La cedula no es valida")