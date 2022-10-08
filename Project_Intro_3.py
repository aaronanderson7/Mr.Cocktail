# Version 3 initializes the data members of the class Ingredient to ask for an input, but I dont
#know if this is the best way to structure our program.

def start_program(all_ingredients, all_garnishes, all_categories):
    """ Starts the cocktail generator program and prints out the list of options for the user.
    :param: all_ingredients = list of all possible ingredients from json file.
    :param: all_garnishes = list of all possible garnishes from json file.
    :param: all_categories = list of all possible categories from json file.
    :return: return the user inputs for user_ingredients_input, user_garnish_input, user_category_input, user_servings_input.
    """

    print("Welcome to Mr. Cocktail! The cocktail recipe generator for those days you don't know what you want to drink."
          "\n From the list of provided ingredients and garnishes, please provide the available ingredients you have on hand,"
          "\n separated by commas.")


class Ingredient:
    """ Defines the user Ingredient object."""

    def __init__(self):
        """ Initialize the data members of class Ingredient.
        attribute: user_ingredients_list = list of user inputted available ingredients
        attribute: user_garnish_list = list of user inputted available garnishes
        attribute: user_category_list = list of user inputted available categories
        attribute: user_servings = int number of servings.
        """
        self._user_ingredients_list = [input("Please enter the ingredients you have on hand\n: ")]
        self._user_garnish_list = [input("Please enter the garnishes you have on hand \n: ")]
        self._user_category_list = [input("Please enter the categories of drinks you would like to enjoy \n: ")]
        self._user_servings = int(input("Please enter how many servings "))

    def get_user_ingredients_list(self, all_ingredients):
        """ Retrieve the current user inputted ingredients.
        :param: all_ingredients = list of all available ingredients from the json file.
        :return: list of user inputted ingredients that are in the all_ingredients list. """

        #Split up the list of ingredients from the user.
        place_holder = self._user_ingredients_list
        self._user_ingredients_list = place_holder.split(", ")

        # Correct for case sensitivity.
        for i in range(len(self._user_ingredients_list)):
            self._user_ingredients_list[i] = self._user_ingredients_list[i].capitalize()

        # Check for ingredients not in all_ingredients list.
        not_user_ingredients_list = [ingredient for ingredient in self._user_ingredients_list if
                                     ingredient not in all_ingredients]
        self._user_ingredients_list = [ingredient for ingredient in all_ingredients if ingredient in self._user_ingredients_list]

        if not_user_ingredients_list != []:
            print("The following ingredients are not in the provided list: \n", not_user_ingredients_list)
        else:
            return self._user_ingredients_list


    def get_user_garnish_list(self, all_garnishes):
        """ Retrieves the current user inputted garnishes:
        :param: all_garnishes = list of all available garnishes from the json file.
        :return: list of user inputted garnishes that are in the all_garnishes list."""

        # Provide the list of all_garnishes from the json file.
        print(all_garnishes)
        user_garnish_input = input("Please enter the garnishes you have on hand \n: ")
        self._user_garnish_list = user_garnish_input.split(", ")

        # Correct for case sensitivity
        for y in range(len(self._user_garnish_list)):
            self._user_garnish_list[y] = self._user_garnish_list[y].capitalize()

        # Check for garnishes not in all_garnishes list.
        not_user_garnish_list = [garnish for garnish in self._user_garnish_list if garnish not in all_garnishes]
        self._user_garnish_list = [garnish for garnish in all_garnishes if garnish in self._user_garnish_list]

        if not_user_garnish_list == [] is False:
            print("The following garnishes are not in the provided list: \n", not_user_garnish_list)
        else:
            return self._user_garnish_list

    def get_user_category_list(self, all_categories):
        """ Retrieves the current user inputted categories:
        :param: all_categories = list of all available categories from the json file.
        :return: list of user inputted categories that are in the all_categories list."""

        #Provide a list of all the categories from the json file.
        print(all_categories)
        user_category_input = input("Please enter the categories of drinks you would like to enjoy \n: ")
        self._user_category_list = user_category_input.split(", ")

        # Correct for case sensitivity.
        for x in range(len(self._user_category_list)):
            self._user_category_list[x] = self._user_category_list[x].capitalize()

        # Check for categories not in all_categories list.
        not_user_category_list = [category for category in self._user_category_list if category not in all_categories]
        self._user_category_list = [category for category in all_categories if category in self._user_category_list]

        if not_user_category_list != []:
            print("The following categories are not in the provided list. \n", not_user_category_list)
        else:
            return self._user_category_list


    def get_user_servings(self):
        """ Retrieves the current user inputted servings:
        :return: the number of user inputted servings."""
        return self._user_servings
