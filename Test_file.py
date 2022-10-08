def start_program(all_ingredients, all_garnishes, all_categories):
    """ Starts the cocktail generator program, and asks for user input parameters.
    :param all_ingredients: list of all possible ingredients
    :param all_garnishes: list of all possible garnishes.
    :param all_categories: list of all possible categories.
    :return: List of all user inputted ingredients, garnishes, and categories.
    """

    user_ingredients_list = []
    user_garnish_list = []
    user_category = []
    user_servings = 1

    print("Welcome to Mr. Cocktail! The cocktail recipe generator for those days you don't know what you want to drink."
          "\n From the list of provided ingredients and garnishes, please provide the available ingredients you have on hand,"
          "\n separated by commas.")

    # Ask for user ingredient input and split up the user string.
    print(all_ingredients)
    user_ingredient_input = input("Please enter the ingredients you have on hand\n: ")
    user_ingredients_list = user_ingredient_input.split(", ")

    # Fix case sensitivity by capitalizing each list element.
    for i in range(len(user_ingredients_list)):
        user_ingredients_list[i] = user_ingredients_list[i].capitalize()

    # Check for ingredients not in all_ingredients list.
    not_user_ingredients_list = [ingredient for ingredient in user_ingredients_list if ingredient not in all_ingredients]
    user_ingredients_list = [ingredient for ingredient in all_ingredients if ingredient in user_ingredients_list]

    if not_user_ingredients_list != []:
        print("The following ingredients are not in the provided list:")
        print(not_user_ingredients_list)
    else:
        return user_ingredients_list


    # Repeat above process for garnishes.
    print(all_garnishes)
    user_garnish_input = input("Please enter the garnishes you have on hand \n: ")
    user_garnish_list = user_garnish_input.split(", ")

    # Fix case sensitivity by capitalizing each list element.
    for y in range(len(user_garnish_list)):
        user_garnish_list[y] = user_garnish_list[y].capitalize()


    # Check for garnishes not in all_garnishes list.
    not_user_garnish_list = [garnish for garnish in user_garnish_list if garnish not in all_garnishes]
    user_garnish_list = [garnish for garnish in all_garnishes if garnish in user_garnish_list]

    if not_user_garnish_list == [] is False:
        print("The following garnishes are not in the provided list:")
        print(not_user_garnish_list)
    else:
        return user_garnish_list


    # Repeat above process for drink category.
    print(all_categories)
    user_category_input = input("Please enter the categories of drinks you would like to enjoy \n: ")
    user_category_list = user_category_input.split(", ")

    # Correct for case sensitivity.
    for x in range(len(user_category_list)):
        user_category_list[x] = user_category_list[x].capitalize()

    # Check for categories not in all_categories list.
    not_user_category_list = [category for category in user_category_list if category  not in all_categories]
    user_category_list = [category for category in all_categories if category in user_category_list]

    if not_user_category_list != []:
        print("The following categories are not in the provided list.")
        print(not_user_category_list)
    else:
        return user_category_list


    # Repeat process for number of desired servings.
    user_servings = int(input("Please enter how many servings "))
    return user_servings





