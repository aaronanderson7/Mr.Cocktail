from ProjectIntro import *
from ParseJSON import *

# Introduces program.
start_program()

# Shows user the categories if desired.
show_categories()

# Gets the desired categories from the user.
user_category_list = get_categories_updated()

# Shows user the ingredients if desired.
show_ingredients()

# Gets the ingredients from the user.
user_ingredient_list = get_ingredients()

# Shows user the garnishes if desired.
show_garnishes()

# Gets the garnishes from the user.
user_garnish_list = get_garnishes_updated()

# Gets the servings from the user.
user_servings = get_servings()

# Returns the possible cocktails the user can make.
cocktail_search(user_ingredient_list, user_garnish_list, user_category_list, user_servings)
