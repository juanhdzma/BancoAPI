from datetime import datetime
from fastapi.encoders import jsonable_encoder
from src.domain.response.StatusCode import StatusCode

class Exception(Exception):
    def __init__(self, message: str, status_code: int):
        self.isError = True
        self.statusCode = status_code
        self.message = message
        self.timestamp = datetime.now()
    
    def serialize(self):
        return jsonable_encoder(self)
    
class BadMessageException(Exception):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.CONFLICT)

class InternalServerErrorException(Exception):
    def __init__(self, message: str):
        super().__init__(message, StatusCode.INTERNAL_SERVER_ERROR)
