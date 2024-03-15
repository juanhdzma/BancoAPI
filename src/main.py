from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from src.domain.response.CustomException import *
from src.domain.response.Response import Response
from src.infrastructure.api.router.AppRouter import banco_router

app = FastAPI()
app.include_router(banco_router, prefix="/BancoV1")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, err: RequestValidationError):
    return Response.failure(BadRequestException(err.errors()[0]['msg']))

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return Response.failure(TeapotException("Uy manito, por aca no era, hmm hmm, digo, I'M A TEAPOT"))

@app.exception_handler(405)
async def custom_405_handler(_, __):
    return Response.failure(TeapotException("Uy manito, por aca no era, hmm hmm, digo, I'M A TEAPOT"))