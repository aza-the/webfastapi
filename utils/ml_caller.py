from .ml.ml import normal_int, run_preditcion_on_model

def ml_call_prediction(
    district_l,
    underground_l,
    underground_time,
    underground_c_by_foot,
    underground_c_by_transport,
    flat_size,
    kitchen_size,
    renovation_c_renovation,
    renovation_c_cosmetic,
    renovation_c_designer,
    renovation_c_no,
    floors_house,
    floor_flat,
    constructed,
    building_c_block_construction,
    building_c_brick_construction,
    building_c_foam_concrete_construction,
    building_c_monolith_brick_construction,
    building_c_monolith_construction,
    building_c_panel_construction,
    building_c_stalins_construction,
    building_c_wooden_construction,
    building_c_idk,
    walls_c_mixed_walls,
    walls_c_reinforced_concrete_walls,
    walls_c_wooden_walls,
    walls_c_idk,
):
    #name of district
    district_l: str = district_l

    # underground information
    underground_l: str = underground_l
    underground_time: int = underground_time
    underground_c_by_foot: bool = underground_c_by_foot
    underground_c_by_transport: bool = underground_c_by_transport
    
    underground_type: str

    if underground_c_by_foot:
        underground_type = 'пешком'
    elif underground_c_by_transport:
        underground_type = 'транспорт'
    else:
        underground_type = "none"

    # flat size information
    flat_size: float = flat_size
    kitchen_size: float = kitchen_size

    # renovation information
    renovation_c_renovation: bool = renovation_c_renovation
    renovation_c_cosmetic: bool = renovation_c_cosmetic
    renovation_c_designer: bool = renovation_c_designer
    renovation_c_no: bool = renovation_c_no

    renovation_type: str

    if renovation_c_renovation:
        renovation_type = 'Евроремонт'
    elif renovation_c_cosmetic:
        renovation_type = 'Косметический'
    elif renovation_c_designer:
        renovation_type = 'Дизайнерский'
    elif renovation_c_no:
        renovation_type = 'Без ремонта'
    else:
        renovation_type = 'None'

    # when was constructed
    floors = floors_house
    floor = floor_flat
    constructed: int = constructed

    # type of building
    building_c_block_construction: bool = building_c_block_construction
    building_c_brick_construction: bool = building_c_brick_construction
    building_c_foam_concrete_construction: bool = building_c_foam_concrete_construction
    building_c_monolith_brick_construction: bool = building_c_monolith_brick_construction
    building_c_monolith_construction: bool = building_c_monolith_construction
    building_c_panel_construction: bool = building_c_panel_construction
    building_c_stalins_construction: bool = building_c_stalins_construction
    building_c_wooden_construction: bool = building_c_wooden_construction
    building_c_idk: bool = building_c_idk

    building_type: str

    if building_c_block_construction:
        building_type = 'Блочный'
    elif building_c_brick_construction:
        building_type = 'Кирпичный'
    elif building_c_foam_concrete_construction:
        building_type = 'Пенобетонный блок'
    elif building_c_monolith_brick_construction:
        building_type = 'Монолитно кирпичный'
    elif building_c_monolith_construction:
        building_type = 'Монолитный'
    elif building_c_panel_construction:
        building_type = 'Панельный'
    elif building_c_stalins_construction:
        building_type = 'Сталинский'
    elif building_c_wooden_construction:
        building_type = 'Деревянный'
    elif building_c_idk:
        building_type = 'None'
    else:
        building_type = 'None'


    # type of walls
    walls_c_mixed_walls: bool = walls_c_mixed_walls
    walls_c_reinforced_concrete_walls: bool = walls_c_reinforced_concrete_walls
    walls_c_wooden_walls: bool = walls_c_wooden_walls
    walls_c_idk: bool = walls_c_idk

    walls_type: str

    if walls_c_mixed_walls:
        walls_type = 'Смешанные'
    elif walls_c_reinforced_concrete_walls:
        walls_type = 'Железобетонные'
    elif walls_c_wooden_walls:
        walls_type = 'Деревянные'
    elif walls_c_idk:
        walls_type = 'None'
    else:
        walls_type = 'None'


    prediction = run_preditcion_on_model(
        district = district_l,
        metro_name = underground_l,
        metro_time = underground_time,
        metro_get_type = underground_type,
        size = flat_size,
        kitchen = kitchen_size,
        floor = floor,
        floors = floors,
        constructed = constructed,
        fix = renovation_type,
        type_of_building = building_type,
        type_of_walls = walls_type,
    )

    prediction = str(normal_int(prediction))

    return prediction