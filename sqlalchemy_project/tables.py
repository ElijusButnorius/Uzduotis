from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'darbuotojai'

    id = Column(Integer, primary_key=True, index=True)
    vardas = Column(String, nullable=False)
    pavarde = Column(String, nullable=False)
    gimimo_data = Column(Date, nullable=False)
    pareigos = Column(String, nullable=False)
    atlyginimas = Column(Float, nullable=False)
    nuo_kada_dirba = Column(Date, nullable=False)
