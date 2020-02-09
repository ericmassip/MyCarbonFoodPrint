from flask import Blueprint, jsonify
from .controller import CountryController

country_service = Blueprint('country_service', __name__)


class CountryService:
    @staticmethod
    @country_service.route('/all')
    def get_all():
        """Get all Countries"""

        return jsonify(CountryController.get_all())

    @staticmethod
    @country_service.route('/carbonfootprint/all/<age_group>/<user_carbon_footprint>')
    def get_all_country_carbon_footprint_by_age_group(age_group, user_carbon_footprint):
        "Get a dictionary with the mean carbon footprint of every country per week for an age group"

        return jsonify(CountryController.get_all_country_carbon_footprint_by_age_group(age_group, user_carbon_footprint))
