from typing import Type, TypeVar, Optional
from src.domain.response.Exceptions import *
from fastapi.responses import JSONResponse
from src.domain.response.Result import *

T = TypeVar('T')

class Response:
    @staticmethod
    def ok(data: Optional[T], statusCode) -> Result:
        response = Result(isError=False, data=data or None)
        return JSONResponse(content=response.serialize(), status_code=statusCode.value)

    @staticmethod
    def failure(exception: Type[Exception]) -> Exception:
        return JSONResponse(content=exception.serialize(), status_code=exception.statusCode.value)
