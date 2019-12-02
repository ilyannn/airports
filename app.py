from config import Config
from flask import Flask, request
from models import db, Airport
from seriailzation import AirportSchema

app = Flask(__name__)
config = Config()
config.perform_configuration(app.config)
db.init_app(app)


airport_serializer = AirportSchema()
airports_serializer = AirportSchema(many=True)


@app.route('/airports')
def get_airports():
    name = request.args.get("name")
    results = Airport.query.filter(Airport.name.contains(name)) if name else Airport.query.all()
    return airports_serializer.jsonify(results)


@app.route('/iata/<code>')
def get_by_iata_code(code):
    results = Airport.query.filter_by(iata_code=code.upper())
    print(results.all())
    return airport_serializer.jsonify(results.first_or_404())


if __name__ == '__main__':
    app.run()
