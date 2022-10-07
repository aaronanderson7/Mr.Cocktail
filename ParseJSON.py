import json

no_ingredients = []
user_ingredients = ["Gin", "Vodka", "Lillet Blonde", "White rum", "Cola", "Lime juice"]
user_garnish = ["Lemon twist", "Lime wedge"]
user_category = "Long Drink"
user_servings = 4


def cocktail_search(user_ingredients_list, user_garnish_list, user_desired_category, user_servings):
    """
    Determines which cocktails in Cocktails.json that the user can make given their input parameters.
    :param user_ingredients_list: List of ingredients from user.
    :param user_garnish_list:  List of garnishes from user.
    :param user_desired_category: Desired category of cocktail for the user.
    :param user_servings: Number of servings the user wants to make.
    :return: Printed list of cocktails with glasses, ingredients, garnishes, and preparation.
    """
    possible_cocktails = dict()
    number_of_cocktails = 0
    with open('Cocktails.json', 'r') as infile:
        cocktails_dict = json.load(infile)
    for entry in cocktails_dict:
        sufficient_ingredients = True
        for ingredient in entry["ingredients"]:
            if "ingredient" in ingredient and sufficient_ingredients is True and ingredient["ingredient"] not in user_ingredients_list:
                sufficient_ingredients = False
        if sufficient_ingredients is True:
            possible_cocktails[entry["name"]] = \
                [entry["glass"], entry["category"], entry["ingredients"], entry["garnish"], entry["preparation"]]
            number_of_cocktails += 1
    if len(possible_cocktails) == 0:
        print("Unfortunately, you do not have the proper ingredients to make any of the cocktails in our recipe book.")
    else:
        print("Congratulations! You can make " + str(number_of_cocktails) + " different cocktails to serve "
                                                                            "your party of " + str(user_servings) +
                                                                            "! Here they are:\n")
        for cocktail in possible_cocktails:
            print(
                cocktail + ":\n" +
                "\t" + "Glass Type: " + possible_cocktails[cocktail][0] + "\n"
                "\t" + "Ingredients: " + "\n"
                "\t" + "Preparation: " + possible_cocktails[cocktail][4] + "\n"
            )


cocktail_search(user_ingredients, user_garnish, user_category, user_servings)
