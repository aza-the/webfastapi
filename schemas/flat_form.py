from pydantic import BaseModel, Field
from fastapi import Form


class FlatForm(BaseModel):

    #name of district
    district_l: str

    # underground information
    underground_l: str
    underground_time: int
    underground_c_by_foot: bool
    underground_c_by_transport: bool

    # flat size information
    flat_size: float
    kitchen_size: float

    # renovation information
    renovation_c_renovation: bool
    renovation_c_cosmetic: bool
    renovation_c_designer: bool
    renovation_c_no: bool

    # when was constructed
    floors_house: int
    floor_flat: int
    constructed: int

    # type of building
    building_c_block_construction: bool
    building_c_brick_construction: bool
    building_c_foam_concrete_construction: bool
    building_c_monolith_brick_construction: bool
    building_c_monolith_construction: bool
    building_c_panel_construction: bool
    building_c_stalins_construction: bool
    building_c_wooden_construction: bool
    building_c_idk: bool

    # type of walls
    walls_c_mixed_walls: bool
    walls_c_reinforced_concrete_walls: bool
    walls_c_wooden_walls: bool
    walls_c_idk: bool


    @classmethod
    def as_form(
        cls,
        #name of district
        district_l: str  = Form('0'),

        # underground information
        underground_l: str  = Form('0'),
        underground_time: int = Form(0),
        underground_c_by_foot: bool = Form(False),
        underground_c_by_transport: bool = Form(False),

        # flat size information
        flat_size: float = Form(.0),
        kitchen_size: float = Form(.0),

        # renovation information
        renovation_c_renovation: bool = Form(False),
        renovation_c_cosmetic: bool = Form(False),
        renovation_c_designer: bool = Form(False),
        renovation_c_no: bool = Form(False),

        # when was constructed
        floors_house: int = Form(0),
        floor_flat: int = Form(0),
        constructed: int = Form(0),

        # type of building
        building_c_block_construction: bool = Form(False),
        building_c_brick_construction: bool = Form(False),
        building_c_foam_concrete_construction: bool = Form(False),
        building_c_monolith_brick_construction: bool = Form(False),
        building_c_monolith_construction: bool = Form(False),
        building_c_panel_construction: bool = Form(False),
        building_c_stalins_construction: bool = Form(False),
        building_c_wooden_construction: bool = Form(False),
        building_c_idk: bool = Form(False),

        # type of walls
        walls_c_mixed_walls: bool = Form(False),
        walls_c_reinforced_concrete_walls: bool = Form(False),
        walls_c_wooden_walls: bool = Form(False),
        walls_c_idk: bool = Form(False),
    ):
        return cls(
            #name of district
            district_l = district_l, 

            # underground in
            underground_l = underground_l, 
            underground_time = underground_time, 
            underground_c_by_foot = underground_c_by_foot, 
            underground_c_by_transport = underground_c_by_transport, 

            # flat size in
            flat_size = flat_size, 
            kitchen_size = kitchen_size, 

            # renovation in
            renovation_c_renovation = renovation_c_renovation, 
            renovation_c_cosmetic = renovation_c_cosmetic, 
            renovation_c_designer = renovation_c_designer, 
            renovation_c_no = renovation_c_no, 

            # when was constructed
            floors_house = floors_house,
            floor_flat = floor_flat,
            constructed = constructed, 

            # type of building
            building_c_block_construction = building_c_block_construction, 
            building_c_brick_construction = building_c_brick_construction, 
            building_c_foam_concrete_construction = building_c_foam_concrete_construction, 
            building_c_monolith_brick_construction = building_c_monolith_brick_construction, 
            building_c_monolith_construction = building_c_monolith_construction, 
            building_c_panel_construction = building_c_panel_construction, 
            building_c_stalins_construction = building_c_stalins_construction, 
            building_c_wooden_construction = building_c_wooden_construction, 
            building_c_idk = building_c_idk, 

            # type of walls
            walls_c_mixed_walls = walls_c_mixed_walls, 
            walls_c_reinforced_concrete_walls = walls_c_reinforced_concrete_walls, 
            walls_c_wooden_walls = walls_c_wooden_walls, 
            walls_c_idk = walls_c_idk, 
        )