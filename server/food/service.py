from flask import Blueprint, jsonify

from .controller import FoodController

food_service = Blueprint('food_service', __name__)


class FoodService:
    @staticmethod
    @food_service.route('/<category>')
    def get_food_items_by_category(category):
        """Get food items filtered by category"""

        return jsonify(FoodController.get_food_items_by_category(category))

    @staticmethod
    @food_service.route('/carbonfootprint/<country>/<age_group>')
    def get_country_carbon_footprint(country, age_group):
        """Get mean carbon footprint of a country per week"""

        return FoodController.get_country_carbon_footprint(country, age_group)
