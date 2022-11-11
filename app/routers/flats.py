import pandas as pd
from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.db import database
from app.schemas.flat_form import FlatForm
from app.utils.ml.ml_caller import ml_call_prediction
from app.utils.ml.table_file_reader import read_df


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(tags=['flats'])

router.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@router.get('/flats/', response_class=HTMLResponse)
async def get_flats_page(request: Request):
    return templates.TemplateResponse("flats/indexrus.html", context={"request": request})

@router.post('/flats/', response_class=HTMLResponse)
async def get_flats_page(request: Request, form_data: FlatForm = Depends(FlatForm.as_form), db: Session = Depends(get_db)):

    prediction = ml_call_prediction(
        db, 
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

    return templates.TemplateResponse("flats/prediction_responserus.html", context={'request': request, 'prediction': prediction})


# test file upload
@router.get('/flats/fileupload')
async def create_file(request: Request):
    return templates.TemplateResponse('flats/create_file.html', context={'request': request})

@router.post("/flats/fileupload")
async def create_upload_file(request: Request, file: UploadFile, db: Session = Depends(get_db)):
    content = await file.read()
    df = pd.read_excel(content)
    df = read_df(df, db)

    df.to_excel('app/static/flats/file_transfer/df_to_excel.xlsx', index=False, header=True)

    return FileResponse('app/static/flats/file_transfer/df_to_excel.xlsx')