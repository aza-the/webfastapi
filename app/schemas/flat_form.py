import json
from fastapi import Form
from pydantic.dataclasses import dataclass
from pydantic import validator
from app.utils.ml.district_converter import find_district
from fastapi import HTTPException


underground_types: tuple = ('пешком', 'транспорт')
renovation_types: tuple = (
    'Без ремонта', 'None', 'Косметический',
    'Дизайнерский', 'Евроремонт'
)
construction_types: tuple = (
    'None', 'Кирпичный', 'Монолитный',
    'Панельный', 'Блочный', 'Монолитно кирпичный',
    'Сталинский', 'Пенобетонный блок', 'Деревянный'
)
wall_types: tuple = ('None', 'Железобетонные', 'Смешанные', 'Деревянные')
METRO_TYPES_PATH = 'app/utils/ml/files_for_ml/metro_name_dict.json'


@dataclass
class FlatForm:
    district: str = Form("")

    underground_station: str = Form("")
    underground_time: int = Form(0)
    underground_get_type: str = Form("")

    num_of_rooms: int = Form(0)
    flat_size: float = Form(0.0)
    kitchen_size: float = Form(0.0)
    storey: int = Form(0)
    storeys: int = Form(0)
    renovation: str = Form("")

    construction_date: int = Form(0)
    construction_type: str = Form("")
    wall: str = Form("")

    @validator('district')
    def validate_district(cls, val):
        return find_district(val)

    @validator('underground_get_type')
    def validate_underground_get_type(cls, val):
        if val not in underground_types:
            raise HTTPException(
                status_code=400,
                detail='Неверный способ добраться до метро'
                f'Доступные способы: {", ".join(underground_types)}'
                f'Ваш вариант: {val}'
                )
        return val

    @validator('underground_time')
    def valudate_underground_time(cls, val):
        if not 0 <= val <= 500:
            raise HTTPException(
                status_code=400,
                detail='Убедитесь, что ввели правильно время, '
                'чтобы добраться до метро'
            )
        return val

    @validator('num_of_rooms')
    def validate_num_of_rooms(cls, val):
        if not 0 <= val <= 3:
            raise HTTPException(
                status_code=400,
                detail='Неверное количество комнат'
            )
        return val

    @validator('flat_size')
    def validate_flat_size(cls, val):
        if not 0 <= val <= 150:
            raise HTTPException(
                status_code=400,
                detail='Неверно введена площадь квартиры.'
                ' Доступно от 0 до 150'
            )
        return val

    @validator('kitchen_size')
    def validate_kitchen_size(cls, val):
        if not 0 <= val <= 70:
            raise HTTPException(
                status_code=400,
                detail='Неверно введена площадь кухни.'
                ' Доступно от 0 до 70'
            )
        return val

    @validator('storey', 'storeys')
    def validate_storey(cls, val):
        if not 0 <= val <= 30:
            raise HTTPException(
                status_code=400,
                detail='Неверно введен(введена) этаж(этажность)'
            )
        return val

    @validator('construction_date')
    def validate_construction_date(cls, val):
        if not 1900 <= val <= 2022:
            raise HTTPException(
                status_code=400,
                detail='Неверно введен год постройки'
            )
        return val

    @validator('renovation')
    def validate_renovation(cls, val):
        if val not in renovation_types:
            raise HTTPException(
                status_code=400,
                detail='Неверная характеристика квартиры.'
                'Доступные характеристики квартиры: '
                f'{" ".join(renovation_types)}'
                f'Ваш вариант: {val}'
                )
        return val

    @validator('underground_station')
    def validate_underground_station(cls, val):
        with open(METRO_TYPES_PATH, 'r', encoding='utf-8') as metro_file:
            data = json.load(metro_file)
        if val not in data:
            raise HTTPException(
                status_code=400,
                detail='Убедитесь в корректности ввода названия метро. '
                'Например: "Шоссе Энтузиастов" "Соколиная гора" '
                f'Ваш вариант: {val}'
            )
        return val

    @validator('construction_type')
    def validate_construction_type(cls, val):
        if val not in construction_types:
            raise HTTPException(
                status_code=400,
                detail='Убедитесь, что данный тип строительных '
                'конструкций существует'
                f'Доступные типы: {" ".join(construction_types)}'
                f'Ваш вариант: {val}'
            )
        return val

    @validator('wall')
    def validate_wall(cls, val):
        if val not in wall_types:
            raise HTTPException(
                status_code=400,
                detail='Неверый тип перекрытий'
                f'Доступные варианты: {" ".join(wall_types)}'
                f'Ваш вариант: {val}'
            )
        return val
