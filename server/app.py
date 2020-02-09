from flask import Flask, escape, request
from flask_cors import CORS
from .country.service import country_service
from .age_group.service import agegroup_service
from .food.service import food_service

app = Flask(__name__)
CORS(app)
app.register_blueprint(country_service, url_prefix='/country')
app.register_blueprint(agegroup_service, url_prefix='/agegroup')
app.register_blueprint(food_service, url_prefix='/food')


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
