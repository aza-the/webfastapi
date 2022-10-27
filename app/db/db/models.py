from sqlalchemy import Column, Integer, String
from .database import Base

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


class Test(Base):
    __tablename__ = 'tests'

    test_id = Column(Integer, primary_key=True)
    test = Column(String)