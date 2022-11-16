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

    underground_station: str = Form("", title='123', examples={'1': 1})
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
                'Неверный способ добраться до метро'
                f'Доступные способы: {", ".join(underground_types)}'
                )
        return val

    @validator('renovation')
    def validate_renovation(cls, val):
        if val not in renovation_types:
            raise HTTPException(
                'Неверная характеристика квартиры.'
                'Доступные характеристики квартиры: '
                f'{" ".join(renovation_types)}'
                )
        return val

    @validator('underground_station')
    def validate_underground_station(cls, val):
        with open(METRO_TYPES_PATH, 'r', encoding='utf-8') as metro_file:
            data = json.loads(metro_file)
        if val not in data:
            raise HTTPException(
                'Убедитесь в корректности ввода названия метро'
                'Например: "Шоссе Энтузиастов" "Соколиная гора"'
            )
        return val

    @validator('construction_type')
    def validate_construction_type(cls, val):
        if val not in construction_types:
            raise HTTPException(
                'Убедитесь, что данный тип строительных '
                'конструкций существует'
                f'Доступные типы: {" ".join(construction_types)}'
            )
        return val

    @validator('wall')
    def validate_wall(cls, val):
        if val not in wall_types:
            raise HTTPException(
                'Неверый тип перекрытий'
                f'Доступные варианты: {" ".join(wall_types)}'
            )
