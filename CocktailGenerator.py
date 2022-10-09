from ProjectIntro import *
from ParseJSON import *
import json

start_program()

show_categories()

user_category_list = get_categories_updated()

show_ingredients()

user_ingredient_list = get_ingredients()

show_garnishes()

user_garnish_list = get_garnishes_updated()

user_servings = get_servings()

cocktail_search(user_ingredient_list, user_garnish_list, user_category_list, user_servings)
