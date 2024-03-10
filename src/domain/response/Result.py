from typing import Type, TypeVar, Optional
from datetime import datetime
from src.domain.response.Exceptions import *
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

T = TypeVar('T')

class Response:
    def __init__(self, isError: bool, data: T, timestamp: datetime):
        self.isError = isError
        self.data = data
        self.timestamp = timestamp

class Result:
    @staticmethod
    def ok(data: Optional[T] = None) -> Response:
        return Response(isError=False, data=data or None, timestamp=datetime.now())

    @staticmethod
    def failure(exception: Type[Exception]) -> Exception:
        respuesta = jsonable_encoder(exception)
        return JSONResponse(content=respuesta, status_code=exception.statusCode.value)
