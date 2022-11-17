import pandas as pd
from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.crud import create_record_flat
from app.schemas import Flat
from app.db.connection import get_session
from app.schemas.flat_form import FlatForm
from app.utils.ml.ml import normal_int, run_preditcion_on_model
from app.utils.ml.table_file_reader import read_df

router = APIRouter(tags=['Flats'])

router.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@router.get('/', response_class=HTMLResponse, include_in_schema=False)
async def get_root(request: Request):
    return templates.TemplateResponse(
        "root/rootrus.html", context={"request": request}
    )


# * Main flats page
@router.get('/flats/', response_class=HTMLResponse, include_in_schema=False)
async def get_flats_page(request: Request):
    return templates.TemplateResponse(
        "flats_up/flats.html", context={"request": request}
    )


@router.post('/flats/')
async def post_flats_page(
    _: Request,
    form_data: FlatForm = Depends(),
    db: Session = Depends(get_session),
):
    prediction = run_preditcion_on_model(
        district=form_data.district,
        metro_name=form_data.underground_station,
        metro_time=form_data.underground_time,
        metro_get_type=form_data.underground_get_type,
        size=form_data.flat_size,
        kitchen=form_data.kitchen_size,
        floor=form_data.storey,
        floors=form_data.storeys,
        constructed=form_data.construction_date,
        fix=form_data.renovation,
        type_of_building=form_data.construction_type,
        type_of_walls=form_data.wall,
    )

    dict_for_pydantic_model_flat = {
        'district': form_data.district,
        'metro_name': form_data.underground_station,
        'metro_time': form_data.underground_time,
        'metro_get_type': form_data.underground_get_type,
        'size': form_data.flat_size,
        'kitchen': form_data.kitchen_size,
        'floor': form_data.storey,
        'floors': form_data.storeys,
        'constructed': form_data.construction_date,
        'fix': form_data.renovation,
        'type_of_building': form_data.construction_type,
        'type_of_walls': form_data.wall,
        'price': int(prediction * 1000000)
        # multiplying by 1 000 000 to get price in millions
    }

    prediction = str(normal_int(prediction))

    try:
        flat = Flat(**dict_for_pydantic_model_flat)
        await create_record_flat(db, flat)
    except Exception as ex:
        print(ex, "POSTGRES OFF HIGH PROBABILITY")

    return {"Итог": prediction}


# * XLSX FILE UPLOADING and RECEIVING page
@router.get('/flats/fileupload', include_in_schema=False)
async def create_file(request: Request):
    return templates.TemplateResponse(
        'flats/create_file.html', context={'request': request}
    )


@router.post("/flats/fileupload")
async def create_upload_file(
    file: UploadFile, db: Session = Depends(get_session)
):
    try:
        content = await file.read()

        df = pd.read_excel(content)
        df = read_df(df, db)
        df.to_excel(
            'app/static/flats/file_transfer/df_to_excel.xlsx',
            index=False,
            header=True,
        )

        return FileResponse('app/static/flats/file_transfer/df_to_excel.xlsx')
    except:
        return FileResponse('app/static/flats/file_transfer/example.xlsx')

@router.get('/flats/example/')
async def get_example_xlsx():
    return FileResponse('app/static/flats/file_transfer/example.xlsx')
