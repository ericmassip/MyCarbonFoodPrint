from flask import Flask

from business_logic.country.service import country_service
from business_logic.food.service import food_service
from business_logic.agegroup.service import agegroup_service


app = Flask(__name__)


app.register_blueprint(country_service, url_prefix='/country')
app.register_blueprint(agegroup_service, url_prefix='/agegroup')
app.register_blueprint(food_service, url_prefix='/food')
