from fastapi import Form
from pydantic.dataclasses import dataclass

@dataclass
class FlatForm():
    #name of district
    district_l: str  = Form('р-н Западный')

    # underground information
    underground_l: str  = Form('Фили')
    underground_time: int = Form(15)
    underground_c_by_foot: bool = Form(True)
    underground_c_by_transport: bool = Form(False)

    # flat size information
    flat_size: float = Form(45.5)
    kitchen_size: float = Form(6.5)

    # renovation information
    renovation_c_renovation: bool = Form(False)
    renovation_c_cosmetic: bool = Form(False)
    renovation_c_designer: bool = Form(False)
    renovation_c_no: bool = Form(True)

    # when was constructed
    floors_house: int = Form(11)
    floor_flat: int = Form(5)
    constructed: int = Form(1993)

    # type of building
    building_c_block_construction: bool = Form(False)
    building_c_brick_construction: bool = Form(False)
    building_c_foam_concrete_construction: bool = Form(False)
    building_c_monolith_brick_construction: bool = Form(False)
    building_c_monolith_construction: bool = Form(False)
    building_c_panel_construction: bool = Form(False)
    building_c_stalins_construction: bool = Form(False)
    building_c_wooden_construction: bool = Form(False)
    building_c_idk: bool = Form(True)

    # type of walls
    walls_c_mixed_walls: bool = Form(False)
    walls_c_reinforced_concrete_walls: bool = Form(False)
    walls_c_wooden_walls: bool = Form(False)
    walls_c_idk: bool = Form(True)