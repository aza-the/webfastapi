from pydantic import BaseModel
from fastapi import Form


class FlatForm(BaseModel):

    #name of district
    district_l: str = 'р-н Западный'

    # underground information
    underground_l: str = 'Фили'
    underground_time: int = '15'
    underground_c_by_foot: bool = True
    underground_c_by_transport: bool = False

    # flat size information
    flat_size: float = '45.5'
    kitchen_size: float = '6.5'

    # renovation information
    renovation_c_renovation: bool = False
    renovation_c_cosmetic: bool = False
    renovation_c_designer: bool = False
    renovation_c_no: bool = True

    # when was constructed
    floors_house: int = 11
    floor_flat: int = 5
    constructed: int = 1993

    # type of building
    building_c_block_construction: bool = False
    building_c_brick_construction: bool = False
    building_c_foam_concrete_construction: bool = False
    building_c_monolith_brick_construction: bool = False
    building_c_monolith_construction: bool = False
    building_c_panel_construction: bool = False
    building_c_stalins_construction: bool = False
    building_c_wooden_construction: bool = False
    building_c_idk: bool = True

    # type of walls
    walls_c_mixed_walls: bool = False
    walls_c_reinforced_concrete_walls: bool = False
    walls_c_wooden_walls: bool = False
    walls_c_idk: bool = True


    @classmethod
    def as_form(
        cls,
        #name of district
        district_l: str  = Form('р-н Западный'),

        # underground information
        underground_l: str  = Form('Фили'),
        underground_time: int = Form(15),
        underground_c_by_foot: bool = Form(True),
        underground_c_by_transport: bool = Form(False),

        # flat size information
        flat_size: float = Form(45.5),
        kitchen_size: float = Form(6.5),

        # renovation information
        renovation_c_renovation: bool = Form(False),
        renovation_c_cosmetic: bool = Form(False),
        renovation_c_designer: bool = Form(False),
        renovation_c_no: bool = Form(True),

        # when was constructed
        floors_house: int = Form(11),
        floor_flat: int = Form(5),
        constructed: int = Form(1993),

        # type of building
        building_c_block_construction: bool = Form(False),
        building_c_brick_construction: bool = Form(False),
        building_c_foam_concrete_construction: bool = Form(False),
        building_c_monolith_brick_construction: bool = Form(False),
        building_c_monolith_construction: bool = Form(False),
        building_c_panel_construction: bool = Form(False),
        building_c_stalins_construction: bool = Form(False),
        building_c_wooden_construction: bool = Form(False),
        building_c_idk: bool = Form(True),

        # type of walls
        walls_c_mixed_walls: bool = Form(False),
        walls_c_reinforced_concrete_walls: bool = Form(False),
        walls_c_wooden_walls: bool = Form(False),
        walls_c_idk: bool = Form(True),
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