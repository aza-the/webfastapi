from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# should be equal to db in alembic.ini
SQLALCHEMY_DATABASE_URL = 'postgresql://flatsuser:password@flats-postgres/flatsdb'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()