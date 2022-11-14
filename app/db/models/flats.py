from sqlalchemy import Column, Float, Integer, String

from app.db.models import DeclarativeBase


class Flats(DeclarativeBase):

    __tablename__ = 'flats'

    id = Column(Integer, primary_key=True, index=True)

    district = Column(String)
    metro_name = Column(String)
    metro_time = Column(String)
    metro_get_type = Column(String)
    size = Column(Float)
    kitchen = Column(Float)
    floor = Column(Integer)
    floors = Column(Integer)
    constructed = Column(Integer)
    fix = Column(String)
    type_of_building = Column(String)
    type_of_walls = Column(String)

    price = Column(Integer)
