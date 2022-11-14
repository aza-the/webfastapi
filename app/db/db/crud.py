from sqlalchemy.orm import Session

from . import models, schemas


def read_record_flat(db: Session, id: int):
    db_flat = db.query(models.Flats).filter(models.Flats.id == id).first()
    return db_flat


def read_records_flat(db: Session, skip: int = 0, limit: int = 100):
    db_flats = db.query(models.Flats).offset(skip).limit(limit).all()
    return db_flats


def create_record_flat(db: Session, flat: schemas.Flat):
    db_flat = models.Flats(**flat.dict())
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat
