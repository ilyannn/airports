from database import Base, engine, db_session
from models import Airport
import csv
import os

Base.metadata.create_all(engine)
s = db_session

basedir = os.path.abspath(os.path.dirname(__file__))
file_name = os.path.join(basedir, "data", "airports.csv")

try:
    with open(file_name) as csv_file:
        for record in csv.reader(csv_file):
            record = [None if v == "\\N" else v for v in record]

            s.add(Airport(
                id=record[0],
                name=record[1],
                city=record[2],
                country=record[3],
                iata_code=record[4],
                icao_code=record[5],
                latitude=record[6],
                longitude=record[7],
                altitude_feet=record[8],
                timezone_offset=record[9],
                timezone_dst=record[10],
                timezone_tz=record[11],
                type=record[12],
                source=record[13]
            ))
    s.commit()
finally:
    s.close()

