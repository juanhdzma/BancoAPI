from fastapi import APIRouter

banco_router = APIRouter()

@banco_router.get("/")
def health_checker():
    return 'Servidor en buen estado'
