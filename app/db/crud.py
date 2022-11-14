from sqlalchemy.orm import Session

from app.db.models import Flats
from app.schemas import Flat


def read_record_flat(db: Session, id: int):
    db_flat = db.query(Flats).filter(Flats.id == id).first()
    return db_flat


def read_records_flat(db: Session, skip: int = 0, limit: int = 100):
    db_flats = db.query(Flats).offset(skip).limit(limit).all()
    return db_flats


def create_record_flat(db: Session, flat: Flat):
    db_flat = Flats(**flat.dict())
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat
