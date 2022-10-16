from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from flat_form import FlatForm

from ml import run_preditcion_on_model, normal_int

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/test')
async def get_test_root(request: Request):
    return templates.TemplateResponse("index1.html", context={"request": request})

@app.get('/')
async def get_root_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.post('/')
async def get_root_page(request: Request, form_data: FlatForm = Depends(FlatForm.as_form)):
    #name of district
    district_l: str = form_data.district_l

    # underground information
    underground_l: str = form_data.underground_l
    underground_time: int = form_data.underground_time
    underground_c_by_foot: bool = form_data.underground_c_by_foot
    underground_c_by_transport: bool = form_data.underground_c_by_transport
    
    underground_type: str

    if underground_c_by_foot:
        underground_type = 'пешком'
    elif underground_c_by_transport:
        underground_type = 'транспорт'
    else:
        underground_type = "none"

    # flat size information
    flat_size: float = form_data.flat_size
    kitchen_size: float = form_data.kitchen_size

    # renovation information
    renovation_c_renovation: bool = form_data.renovation_c_renovation
    renovation_c_cosmetic: bool = form_data.renovation_c_cosmetic
    renovation_c_designer: bool = form_data.renovation_c_designer
    renovation_c_no: bool = form_data.renovation_c_no

    renovation_type: str

    if renovation_c_renovation:
        renovation_type = 'Евроремонт'
    elif renovation_c_cosmetic:
        renovation_type = 'Косметический'
    elif renovation_c_designer:
        renovation_type = 'Дизайнерский'
    elif renovation_c_no:
        renovation_type = 'Без ремонта'
    else:
        renovation_type = 'None'

    # when was constructed
    floors = form_data.floors_house
    floor = form_data.floor_flat
    constructed: int = form_data.constructed

    # type of building
    building_c_block_construction: bool = form_data.building_c_block_construction
    building_c_brick_construction: bool = form_data.building_c_brick_construction
    building_c_foam_concrete_construction: bool = form_data.building_c_foam_concrete_construction
    building_c_monolith_brick_construction: bool = form_data.building_c_monolith_brick_construction
    building_c_monolith_construction: bool = form_data.building_c_monolith_construction
    building_c_panel_construction: bool = form_data.building_c_panel_construction
    building_c_stalins_construction: bool = form_data.building_c_stalins_construction
    building_c_wooden_construction: bool = form_data.building_c_wooden_construction
    building_c_idk: bool = form_data.building_c_idk

    building_type: str

    if building_c_block_construction:
        building_type = 'Блочный'
    elif building_c_brick_construction:
        building_type = 'Кирпичный'
    elif building_c_foam_concrete_construction:
        building_type = 'Пенобетонный блок'
    elif building_c_monolith_brick_construction:
        building_type = 'Монолитно кирпичный'
    elif building_c_monolith_construction:
        building_type = 'Монолитный'
    elif building_c_panel_construction:
        building_type = 'Панельный'
    elif building_c_stalins_construction:
        building_type = 'Сталинский'
    elif building_c_wooden_construction:
        building_type = 'Деревянный'
    elif building_c_idk:
        building_type = 'None'
    else:
        building_type = 'None'


    # type of walls
    walls_c_mixed_walls: bool = form_data.walls_c_mixed_walls
    walls_c_reinforced_concrete_walls: bool = form_data.walls_c_reinforced_concrete_walls
    walls_c_wooden_walls: bool = form_data.walls_c_wooden_walls
    walls_c_idk: bool = form_data.walls_c_idk

    walls_type: str

    if walls_c_mixed_walls:
        walls_type = 'Смешанные'
    elif walls_c_reinforced_concrete_walls:
        walls_type = 'Железобетонные'
    elif walls_c_wooden_walls:
        walls_type = 'Деревянные'
    elif walls_c_idk:
        walls_type = 'None'
    else:
        walls_type = 'None'


    prediction = run_preditcion_on_model(
        district = district_l,
        metro_name = underground_l,
        metro_time = underground_time,
        metro_get_type = underground_type,
        size = flat_size,
        kitchen = kitchen_size,
        floor = floor,
        floors = floors,
        constructed = constructed,
        fix = renovation_type,
        type_of_building = building_type,
        type_of_walls = walls_type,
    )

    prediction = str(normal_int(prediction))

    return templates.TemplateResponse("prediction_response.html", context={'request': request, 'prediction': prediction})