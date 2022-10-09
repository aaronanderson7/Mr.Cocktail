# I think this version is a better option, and I question if we even need to use an Ingredient Object?
import json


def start_program():
    """ Starts the cocktail generator program."""
    # Program Introduction
    print("Welcome to Mr. Cocktail! The cocktail recipe generator for those days you don't know what you want to drink."
          "\n From the list of provided ingredients and garnishes, please provide the "
          "\n available ingredients you have on hand separated by commas and a space.")


def get_ingredients():
    """ Gathers the users inputted available ingredients for cocktails.
    :return: user_ingredients_list = list of user inputted available ingredients that they have on hand.
    """

    # Create the list of all possible ingredients from JSON file.
    all_ingredients = []
    with open('Cocktails.json', 'r') as infile:
        cocktails_dict = json.load(infile)

    # Add each possible garnish from the JSON file to all_garnishes.
    for cocktail in cocktails_dict:
        for ingredient in cocktail["ingredients"]:
            if "ingredient" in ingredient and ingredient["ingredient"] not in all_ingredients:
                all_ingredients.append(ingredient["ingredient"])

    # Ask for user ingredient input and split up the user string, ing = ingredient
    user_ingredients_list = [ing for ing in input("Please enter the ingredients you have on hand, "
                                                  "separated by commas. \n: ").split(", ")]

    # Fix case sensitivity by capitalizing each list element.
    for x in range(len(user_ingredients_list)):
        user_ingredients_list[x] = user_ingredients_list[x].capitalize()

    # Check for ingredients not in all_ingredients list.
    not_user_ingredients_list = [ing for ing in user_ingredients_list if ing not in all_ingredients]
    user_ingredients_list = [ing for ing in all_ingredients if ing in user_ingredients_list]
    if not_user_ingredients_list != []:
        print("The following ingredients are not in the provided list: \n", not_user_ingredients_list)

    # Show user the current list of ingredients, check if user wants to add more.
    print("Here are your listed ingredients:\n ", user_ingredients_list)
    question = input("Would you like to add more ingredients? (Yes / No): ")

    # User can continually add to the list of ingredients.
    while question.capitalize() == "Yes":
        added_ingredients_list = [ing for ing in input("Please enter additional ingredients\n: ").split(", ")]
        for x in range(len(added_ingredients_list)):
            added_ingredients_list[x] = added_ingredients_list[x].capitalize()
        for ing in added_ingredients_list:
            if ing not in all_ingredients:
                print(f"{ing} is not in the list of possible ingredients.")
            elif ing in user_ingredients_list:
                print(f"{ing} is already in your list of ingredients.")
            else:
                user_ingredients_list.append(ing)
        print("Here is your updated list of ingredients:\n ", user_ingredients_list)
        question = input("Would you like to add more ingredients? (Yes / No): ")
    return user_ingredients_list


def get_garnishes_updated():
    """ Gathers the users inputted available garnishes for cocktails.
    :return: user_garnishes_list = list of user inputted available garnishes that they have on hand.
    """
    # Create the list of all possible garnishes from JSON file.
    all_garnishes = []
    with open('Cocktails.json', 'r') as infile:
        cocktails_dict = json.load(infile)

    # Add each possible garnish from the JSON file to all_garnishes.
    for cocktail in cocktails_dict:
        if "garnish" in cocktail and cocktail["garnish"] not in all_garnishes:
            all_garnishes.append(cocktail["garnish"])

    # Ask for user garnish input and split up the user string, ing = ingredient
    user_garnishes_list = [ing for ing in input("Please enter the garnishes you have on hand, "
                                                "separated by commas. \n: ").split(", ")]

    # Fix case sensitivity by capitalizing each list element.
    for x in range(len(user_garnishes_list)):
        user_garnishes_list[x] = user_garnishes_list[x].capitalize()

    # Check for garnishes not in all_garnishes list.
    not_user_garnishes_list = [ing for ing in user_garnishes_list if ing not in all_garnishes]
    user_garnishes_list = [ing for ing in all_garnishes if ing in user_garnishes_list]
    if not_user_garnishes_list != []:
        print("The following garnishes are not in the provided list: \n", not_user_garnishes_list)

    # Show user the current list of garnishes, check if user wants to add more.
    print("Here are your listed garnishes:\n ", user_garnishes_list)
    question = input("Would you like to add more garnishes? (Yes / No): ")

    # User can continually add to the list of garnishes.
    while question.capitalize() == "Yes":
        added_garnishes_list = [ing for ing in input("Please enter additional garnishes\n: ").split(", ")]
        for x in range(len(added_garnishes_list)):
            added_garnishes_list[x] = added_garnishes_list[x].capitalize()
        for ing in added_garnishes_list:
            if ing not in all_garnishes:
                print(f"{ing} is not in the list of possible garnishes.")
            elif ing in user_garnishes_list:
                print(f"{ing} is already in your list of garnishes.")
            else:
                user_garnishes_list.append(ing)
        print("Here is your updated list of garnishes:\n ", user_garnishes_list)
        question = input("Would you like to add more garnishes? (Yes / No): ")
    return user_garnishes_list


def get_categories_updated():
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_categories = list of all possible categories from json file.
    :return: user_categories_list = list of user inputted available categories that they have on hand.
    """

    all_categories = []

    # Open the Cocktails.json file to read.
    with open('Cocktails.json', 'r') as infile:
        cocktails_dict = json.load(infile)

    # Add each possible category from the JSON file to all_garnishes.
    for cocktail in cocktails_dict:
        if "category" in cocktail and cocktail["category"] not in all_categories:
            all_categories.append(cocktail["category"])

    # Ask for user category input and split up the user string, ing = ingredient
    user_categories_list = [ing for ing in input("Please enter the categories you would like, "
                                                 "separated by commas. \n: ").split(", ")]

    # Check for categories not in all_categories list.
    not_user_categories_list = [ing for ing in user_categories_list if ing not in all_categories]
    user_categories_list = [ing for ing in all_categories if ing in user_categories_list]
    if not_user_categories_list != []:
        print("The following categories are not in the provided list: \n", not_user_categories_list)

    # Show user the current list of garnishes, check if user wants to add more.
    print("Here are your listed categories:\n ", user_categories_list)
    question = input("Would you like to add more categories? (Yes / No): ")

    # User can continually add to the list of categories.
    while question.capitalize() == "Yes":
        added_categories_list = [ing for ing in input("Please enter additional categories\n: ").split(", ")]
        for ing in added_categories_list:
            if ing not in all_categories:
                print(f"{ing} is not in the list of possible categories.")
            elif ing in user_categories_list:
                print(f"{ing} is already in your list of categories.")
            else:
                user_categories_list.append(ing)
        print("Here is your updated list of categories:\n ", user_categories_list)
        question = input("Would you like to add more categories? (Yes / No): ")
    return user_categories_list


def get_servings():
    """ Starts the cocktail generator program and gathers the users inputted available materials for cocktails.
    :param: all_categories = list of all possible categories from json file.
    :return: user_categories_list = list of user inputted available categories that they have on hand.
    """
    # Input for number of desired servings.
    user_servings = input("\nPlease enter how many servings (e.g. 1, 2, 3, etc.): ")
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
