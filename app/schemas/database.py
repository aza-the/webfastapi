from pydantic import BaseModel

class Flat(BaseModel):

    district: str
    metro_name: str
    metro_time: str
    metro_get_type: str
    size: float
    kitchen: float
    floor: int
    floors: int
    constructed: int
    fix: str
    type_of_building: str
    type_of_walls: str

    price: int