from ..food.controller import FoodController
from ..utils.config import COUNTRIES


class CountryController:
    @staticmethod
    def get_all():
        """Get all Countries"""

        return COUNTRIES

    @staticmethod
    def get_all_country_carbon_footprint_by_age_group(age_group, user_carbon_footprint):
        "Get a dictionary with the mean carbon footprint of every country per week for an age group"

        countries = CountryController.get_all()
        countries = list(
            map(lambda x: {'name': x,
                           'carbonFootprint': float(FoodController.get_country_carbon_footprint(x, age_group))},
                countries))
        countries += [{'name': 'YOU', 'carbonFootprint': float(user_carbon_footprint)}]

        return sorted(countries, key=lambda i: i['carbonFootprint'])
