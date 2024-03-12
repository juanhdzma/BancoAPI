from typing import Type, TypeVar
from fastapi.responses import JSONResponse
from src.domain.response.Result import *

T = TypeVar('T')

class Response:
    @staticmethod
    def ok(data: T) -> Result:
        return JSONResponse(content=data.serialize(), status_code=data.statusCode.value)

    @staticmethod
    def failure(exception: Type[Exception]) -> Exception:
        return JSONResponse(content=exception.serialize(), status_code=exception.statusCode.value)
