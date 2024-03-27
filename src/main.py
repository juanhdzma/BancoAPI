from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
import yaml
from src.domain.response.CustomException import *
from src.domain.response.Response import Response
from src.infrastructure.api.router.AppRouter import banco_router

app = FastAPI()
app.include_router(banco_router, prefix="/BancoV1")

# Load your YAML OpenAPI file
with open("docs/swagger/bancoAPI.yaml", "r") as file:
    openapi_yaml_content = yaml.safe_load(file)

def custom_openapi():
    return openapi_yaml_content
app.openapi = custom_openapi

@app.get("/docs", response_class=PlainTextResponse)
async def read_openapi():
    return yaml.dump(openapi_yaml_content)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, err: RequestValidationError):
    return Response.failure(BadRequestException(err.errors()[0]['msg']))

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return Response.failure(NotFoundException("Ruta no encontrada"))

@app.exception_handler(405)
async def custom_405_handler(_, __):
    return Response.failure(NotFoundException("Metodo incorrecto"))