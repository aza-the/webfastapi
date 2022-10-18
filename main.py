from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas.flat_form import FlatForm
from utils.ml_caller import ml_call_prediction

from routers import list_of_routes

app = FastAPI()
for route in list_of_routes:
    app.include_router(route)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get_root(request: Request):
    return templates.TemplateResponse("root.html", context={"request": request})