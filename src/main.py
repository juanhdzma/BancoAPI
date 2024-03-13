from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from src.domain.response.CustomException import BadRequestException
from src.domain.response.Response import Response
from src.infrastructure.api.routers.AppRouter import banco_router

app = FastAPI()
app.include_router(banco_router, prefix="/BancoV1")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, err: RequestValidationError):
    return Response.failure(BadRequestException(err.errors()[0]['msg']))
