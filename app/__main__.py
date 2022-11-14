from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import list_of_routes

app = FastAPI()
for route in list_of_routes:
    app.include_router(route)

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse(
        "error404/error404rus.html", context={"request": request}
    )


@app.get('/', response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse(
        "root/rootrus.html", context={"request": request}
    )
