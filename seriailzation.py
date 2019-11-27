from flask_marshmallow import Schema
from marshmallow.fields import Float, Integer, String
from models import Airport


class AirportSchema(Schema):

    iata = String(attribute="iata_code")
    icao = String(attribute="icao_code")

    class Meta:
        model = Airport
        fields = ("name", "city", "country", "iata", "icao", "longitude", "latitude")