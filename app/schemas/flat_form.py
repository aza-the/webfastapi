from fastapi import Form
from pydantic.dataclasses import dataclass


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
