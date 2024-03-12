from datetime import datetime
from fastapi.encoders import jsonable_encoder
from src.domain.response.StatusCode import StatusCode

class Exception(Exception):
    def __init__(self, message: str, statusCode: int):
        self.isError = True
        self.message = message
        self.statusCode = statusCode
        self.timestamp = datetime.now()
    
    def serialize(self):
        return jsonable_encoder(self)
    

class BadRequestException(Exception):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.BAD_REQUEST)    
class ConflictException(Exception):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.CONFLICT)

class InternalServerErrorException(Exception):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.INTERNAL_SERVER_ERROR)
