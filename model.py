from sqlalchemy import Column, Float, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True)
    value = Column(Float(53), nullable=False)
    index = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)


class Output(Base):
    __tablename__ = 'outputs'

    id = Column(Integer, primary_key=True)
    value = Column(Float(53), nullable=False)
    index = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)


def get_base():
    return Base