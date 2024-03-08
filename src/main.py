from fastapi import FastAPI
from src.infrastructure.api.routers.AppRouter import banco_router

app = FastAPI()

app.include_router(banco_router, prefix="/BancoV1")
