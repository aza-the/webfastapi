import pandas as pd
from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.connection import get_session
from app.schemas.flat_form import FlatForm
from app.utils.ml.ml_caller import ml_call_prediction
from app.utils.ml.table_file_reader import read_df

router = APIRouter(tags=['flats'])

router.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


# * Main flats page
@router.get('/flats/', response_class=HTMLResponse)
async def get_flats_page(request: Request):
    return templates.TemplateResponse(
        "flats_up/flats.html", context={"request": request}
    )


@router.post('/flats/', response_class=HTMLResponse)
async def post_flats_page(
    request: Request,
    form_data: FlatForm = Depends(),
    db: Session = Depends(get_session),
):
    prediction = ml_call_prediction(
        db,
    )
    return templates.TemplateResponse(
        "flats/prediction_responserus.html",
        context={'request': request, 'prediction': prediction},
    )


# * XLSX FILE UPLOADING and RECEIVING page
@router.get('/flats/fileupload')
async def create_file(request: Request):
    return templates.TemplateResponse(
        'flats/create_file.html', context={'request': request}
    )


@router.post("/flats/fileupload")
async def create_upload_file(
    file: UploadFile, db: Session = Depends(get_session)
):
    content = await file.read()

    df = pd.read_excel(content)
    df = read_df(df, db)
    df.to_excel(
        'app/static/flats/file_transfer/df_to_excel.xlsx',
        index=False,
        header=True,
    )

    return FileResponse('app/static/flats/file_transfer/df_to_excel.xlsx')


@router.get('/flats/example/')
async def get_example_xlsx():
    return FileResponse('app/static/flats/file_transfer/example.xlsx')
