from ..utils.config import FOOD_CATEGORY_ITEMS, co2_per_country_age_group


class FoodController:
    @staticmethod
    def get_food_items_by_category(category):
        """Get food items filtered by category"""

        return list(map(lambda food_item: food_item.__dict__, FOOD_CATEGORY_ITEMS[category]))

    @staticmethod
    def get_country_carbon_footprint(country, age_group):
        """Get mean carbon footprint of a country per week"""

        df = co2_per_country_age_group
        country_carbon_footprint = (df[(df["Country"] == country) & (df["ageGroup"] == age_group)]["Mean_CO2.g"].values[
                                        0] * 7) / 1000
        return str(f'{country_carbon_footprint:.1f}')
