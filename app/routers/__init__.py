from app.routers.flats import router as flats_router
from app.routers.health_check import api_router as health_check_router

list_of_routes = [flats_router, health_check_router]

__all__ = ['list_of_routes']
