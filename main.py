from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas.flat_form import FlatForm

from utils.ml.ml import run_preditcion_on_model, normal_int
from utils.ml_caller import ml_call_prediction

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get_flats_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.post('/')
async def get_flats_page(request: Request, form_data: FlatForm = Depends(FlatForm.as_form)):

    prediction = ml_call_prediction(
        form_data.district_l,
        form_data.underground_l,
        form_data.underground_time,
        form_data.underground_c_by_foot,
        form_data.underground_c_by_transport,
        form_data.flat_size,
        form_data.kitchen_size,
        form_data.renovation_c_renovation,
        form_data.renovation_c_cosmetic,
        form_data.renovation_c_designer,
        form_data.renovation_c_no,
        form_data.floors_house,
        form_data.floor_flat,
        form_data.constructed,
        form_data.building_c_block_construction,
        form_data.building_c_brick_construction,
        form_data.building_c_foam_concrete_construction,
        form_data.building_c_monolith_brick_construction,
        form_data.building_c_monolith_construction,
        form_data.building_c_panel_construction,
        form_data.building_c_stalins_construction,
        form_data.building_c_wooden_construction,
        form_data.building_c_idk,
        form_data.walls_c_mixed_walls,
        form_data.walls_c_reinforced_concrete_walls,
        form_data.walls_c_wooden_walls,
        form_data.walls_c_idk,
    )

    return templates.TemplateResponse("prediction_response.html", context={'request': request, 'prediction': prediction})