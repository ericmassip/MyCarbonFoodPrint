import pandas as pd
from business_logic.food.model import FoodItem

co2_per_country_age_group = pd.read_csv('dataset/co2_per_country_age_group.csv')
co2_footprint = pd.read_csv('dataset/co2_footprint.csv', index_col='ID')
co2_footprint['Category'] = co2_footprint['Category'].apply(lambda x: x.replace("/", "_"))

COUNTRIES = co2_per_country_age_group['Country'].unique().tolist()
AGE_GROUPS = co2_per_country_age_group['ageGroup'].unique().tolist()
FOOD_CATEGORY_ITEMS = {}

for i in co2_footprint.index:
    category = co2_footprint.at[i, 'Category']
    food = co2_footprint.at[i, 'Food']
    grams_co2_per_serving = co2_footprint.at[i, 'Grams.CO2e.per.Serving']

    if category not in FOOD_CATEGORY_ITEMS:
        FOOD_CATEGORY_ITEMS[category] = []

    food_item = FoodItem(food, grams_co2_per_serving)
    FOOD_CATEGORY_ITEMS[category].append(food_item)