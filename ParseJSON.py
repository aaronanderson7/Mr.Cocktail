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
    # Initialize the possible cocktails and number of possible cocktails.
    possible_cocktails = dict()
    number_of_cocktails = 0

    # Open the Cocktails.json file to read.
    with open('Cocktails.json', 'r') as infile:
        cocktails_dict = json.load(infile)
    # Search the JSON file for the ingredients in user_ingredients_list.

    for entry in cocktails_dict:
        sufficient_ingredients = True
        for ingredient in entry["ingredients"]:
            # When an ingredient is a part of a cocktail, user does not have sufficient ingredients.
            if "ingredient" in ingredient and sufficient_ingredients is True and ingredient["ingredient"] not in user_ingredients_list:
                sufficient_ingredients = False
        # User has sufficient ingredients for given cocktail, add to the dictionary of possible cocktails.
        if sufficient_ingredients is True:
            possible_cocktails[entry["name"]] = \
                [entry["glass"], entry["category"], entry["ingredients"], entry["garnish"], entry["preparation"]]
            number_of_cocktails += 1

    # If user does not have enough ingredients for any cocktails, prints out following message.
    if len(possible_cocktails) == 0:
        print("Unfortunately, your listed ingredients are not sufficient to make any of the cocktails in our recipe book.")
    # User can make certain cocktails, prints out cocktail names and corresponding information.
    else:
        print(f"Party time! You can make {str(number_of_cocktails)} different cocktails to serve your group "
              f"of {str(user_servings)}! Here they are:\n")
        for cocktail in possible_cocktails:
            print(
                cocktail + ":\n" +
                "\t" + "Category: " + possible_cocktails[cocktail][1] + "\n"
                "\t" + "Glass Type: " + possible_cocktails[cocktail][0] + "\n"
                "\t" + f"Ingredients to Serve {user_servings}: "
            )
            for items in possible_cocktails[cocktail][2]:
                if "amount" in items:
                    amount = round(user_servings * items["amount"] * 0.33814, 1)
                    ingredient = str(items["ingredient"])
                    print("\t" + "\t" + f"{str(amount)} fl oz of {ingredient}")
                if "special" in items:
                    # Convert first digit in to match number of servings.
                    if items["special"][0].isdigit() is True:
                        items["special"] = str(4 * int(items["special"][0])) + items["special"][1:]
                    special = str(items["special"])
                    print("\t" + "\t" + f"{special}")
            print(
                "\t" + "Garnish: " + possible_cocktails[cocktail][3] + "\n"
                "\t" + "Preparation: " + possible_cocktails[cocktail][4] + "\n"
            )
    # print(possible_cocktails)

cocktail_search(user_ingredients, user_garnish, user_category, user_servings)
