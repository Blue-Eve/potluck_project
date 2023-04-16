# import preproc fn

from potluck_code.preprocessor import preproc_ingredients


# extend user input by the most similar ingredients found in the model


def extend_input(user_input, model, k):
    extended_input = set()
    for ingredient in user_input:
        extended_input.add(ingredient)
        search_ingredient = ingredient
        found = False
        while not found:
            try:
                k_nearest_ingredients = model.wv.most_similar(search_ingredient, topn=k)
                extended_input.add(search_ingredient)
                extended_input = extended_input.union(
                    {i[0] for i in k_nearest_ingredients}
                )
                found = True
            except KeyError:
                try:
                    search_ingredient = search_ingredient.split("_", maxsplit=1)[1]
                except:
                    break
    return extended_input


# define search function


def recipe_search(model, df, user_input, k):
    # preprocess
    preprocced_input = preproc_ingredients(user_input + ["salt", "pepper", "water"])

    if k == 0:
        # search without extending
        recipe_df = df[
            df["search_ingredients"].apply(lambda x: x.issubset(preprocced_input))
        ]
    else:
        # extend
        k_input = extend_input(preprocced_input, model, k)
        recipe_df = df[
            df["search_in_space_ingredients"].apply(lambda x: x.issubset(k_input))
        ]

    recipe_df["input_matching_rate"] = recipe_df["search_ingredients"].apply(
        lambda x: len(x.intersection(preprocced_input))
    ) / len(preprocced_input)
    return recipe_df.sort_values(
        ["input_matching_rate", "avg_rating"], ascending=[False, False]
    ).iloc[:16]
