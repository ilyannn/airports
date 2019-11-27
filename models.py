from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String

db = SQLAlchemy()


class Airport(db.Model):
    __tablename__ = 'Airports'
    id = Column(Integer, primary_key = True)
    name = Column(String(1000), nullable=False)

    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)

    iata_code = Column(String(3), nullable=True, index=True)
    icao_code = Column(String(4), nullable=True, index=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude_feet = Column(Float, nullable=False)

    timezone_offset = Column(Float(asdecimal=True), nullable=True)
    timezone_dst = Column(String(1), nullable=True)
    timezone_tz = Column(String(29), nullable=True)

    type = Column(String(20), nullable=False)
    source = Column(String(20), nullable=False)
