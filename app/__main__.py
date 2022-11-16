from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import get_settings
from app.config import DefaultSettings

from app.routers import list_of_routes

settings = get_settings()


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    """Bind all Routes"""
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = (
        'Сервис для расчета рыночной стоимости '
        'жилой недвижимости Города Москвы'
    )

    tags_metadata = [
        {
            'name': 'Health check',
            'description': 'API health check.'
        },
        {
            'name': 'Flats',
            'description': 'Analysis cost of houses'
        }
    ]

    application = FastAPI(
        title='WebFastAPI',
        description=description,
        docs_url='/swagger',
        redoc_url='/redoc',
        openapi_url='/openapi',
        openapi_tags=tags_metadata,
    )
    bind_routes(application, settings)
    application.state.settings = settings

    application.mount(
        "/app/static", StaticFiles(directory="app/static"), name="static"
    )
    return application


app = get_app()
templates = Jinja2Templates(directory="app/templates")


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse(
        "error404/error404rus.html", context={"request": request}
    )
