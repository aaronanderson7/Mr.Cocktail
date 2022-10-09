# I think this version is a better option, and I question if we even need to use an Ingredient Object?

def start_program(all_ingredients, all_garnishes, all_categories):
    """ Starts the cocktail generator program."""
    # Program Introduction
    print("Welcome to Mr. Cocktail! The cocktail recipe generator for those days you don't know what you want to drink."
          "\n From the list of provided ingredients and garnishes, please provide the "
          "\n available ingredients you have on hand separated by commas and a space.")

def get_ingredients(all_ingredients):
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_ingredients = list of all possible ingredients from json file.
    :return: user_ingredients_list = list of user inputted available ingredients that they have on hand.
    """
    # Ask for user ingredient input and split up the user string, ing = ingredient
    print("Ingredients: \n", all_ingredients)
    user_ingredients_list = [ing for ing in input("Please enter the ingredients you have on hand\n: ").split(", ")]

    # Fix case sensitivity by capitalizing each list element.
    for x in range(len(user_ingredients_list)):
        user_ingredients_list[x] = user_ingredients_list[x].capitalize()

    # Check for ingredients not in all_ingredients list.
    not_user_ingredients_list = [ing for ing in user_ingredients_list if ing not in all_ingredients]
    user_ingredients_list = [ing for ing in all_ingredients if ing in user_ingredients_list]

    if not_user_ingredients_list != []:
        print("The following ingredients are not in the provided list: \n", not_user_ingredients_list)

    print("Here are your listed ingredients:\n ", user_ingredients_list)
    question = input("Would you like to add more ingredients? (Yes / No): ")
    if question.capitalize() == "Yes":
        added_ingredients_list = [ing for ing in input("Please enter additional categories\n: ").split(", ")]
        for x in range(len(added_ingredients_list)):
            added_ingredients_list[x] = added_ingredients_list[x].capitalize()
        for ing in added_ingredients_list:
            if ing not in user_ingredients_list:
                user_ingredients_list.append(ing)
    return user_ingredients_list

def get_garnishes(all_garnishes):
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_garnishes = list of all possible garnishes from json file.
    :return: user_ingredients_list = list of user inputted available garnishes that they have on hand.
    """
    # Repeat above process for garnishes, gar = garnish
    print("Garnishes: \n", all_garnishes)
    user_garnish_list = [gar for gar in input("Please enter the garnishes you have on hand\n: ").split(", ")]

    # Fix case sensitivity by capitalizing each list element.
    for x in range(len(user_garnish_list)):
        user_garnish_list[x] = user_garnish_list[x].capitalize()

    # Check for garnishes not in all_garnishes list.
    not_user_garnish_list = [gar for gar in user_garnish_list if gar not in all_garnishes]
    user_garnish_list = [gar for gar in all_garnishes if gar in user_garnish_list]

    if not_user_garnish_list != []:
        print("The following garnishes are not in the provided list: \n", not_user_garnish_list)

    print("Here are your listed garnishes:\n ", user_garnish_list)
    question = input("Would you like to add more garnishes? (Yes / No): ")
    if question.capitalize() == "Yes":
        added_garnish_list = [gar for gar in input("Please enter additional garnishes\n: ").split(", ")]
        for x in range(len(added_garnish_list)):
            added_garnish_list[x] = added_garnish_list[x].capitalize()
        for gar in added_garnish_list:
            if gar not in user_garnish_list:
                user_garnish_list.append(gar)
    return user_garnish_list

def get_categories():
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_categories = list of all possible categories from json file.
    :return: user_categories_list = list of user inputted available categories that they have on hand.
    """
    # Repeat above process for drink category.
    print("Categories: \n", all_categories)
    user_category_list = [cat for cat in input("Please enter the drink categories\n: ").split(", ")]

    # Correct for case sensitivity.
    for x in range(len(user_category_list)):
        user_category_list[x] = user_category_list[x].capitalize()

    # Check for categories not in all_categories list, cat = category
    not_user_category_list = [cat for cat in user_category_list if cat not in all_categories]
    user_category_list = [cat for cat in all_categories if cat in user_category_list]

    if not_user_category_list != []:
        print("The following categories are not in the provided list. \n", not_user_category_list)

    print("Here are your listed categories:\n ", user_category_list)
    question = input("Would you like to add more categories? (Yes / No): ")
    if question.capitalize() == "Yes":
        added_category_list = [cat for cat in input("Please enter additional categories\n: ").split(", ")]
        for x in range(len(added_category_list)):
            added_category_list[x] = added_category_list[x].capitalize()
        for cat in added_category_list:
            if cat not in user_category_list:
                user_category_list.append(cat)
    return user_category_list

def get_servings():
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_categories = list of all possible categories from json file.
    :return: user_categories_list = list of user inputted available categories that they have on hand.
    """
    # Input for number of desired servings.
    user_servings = input("Please enter how many servings: ")
    return int(user_servings)

# Do we even need an ingredient object?
class Ingredient:
    """ Represents a unique Ingredient object.
    :attribute: user_ingredients_list = list of user inputted ingredient garnishes
    :attribute: user_garnish_list = list of user inputted garnishes
    :attribute: user_category_list = list of user inputted drink categories.
    :attribute: user_servings = number of user inputted servings.
    """

    def __init__(self, user_ingredients_list, user_garnish_list, user_category_list, user_servings):
        """ Initialize the data members."""
        self._user_ingredients_list = user_ingredients_list
        self._user_garnish_list = user_garnish_list
        self._user_category_list = user_category_list
        self._user_servings = user_servings

    def get_user_ingredients_list(self):
        """" Retrieve the current user_ingredients_list"""
        return self._user_ingredients_list

    def get_user_garnish_list(self):
        return self._user_garnish_list

    def get_user_category_list(self):
        return self._user_category_list

    def get_user_servings(self):
        return self._user_servings
