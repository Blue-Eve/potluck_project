######################### NLP #########################
import string
from nltk.stem import WordNetLemmatizer


def remove_num(text):
    return "".join(char for char in text if not char.isdigit())


def remove_punctuation(ingredients):
    cleaned_list = []
    for word in ingredients:
        for punctuation in string.punctuation:
            word = word.replace(punctuation, "")
        cleaned_list.append(word)
    return cleaned_list


def lemmatize_ingredients(ingredients):
    lemmatized = []
    for ingredient in ingredients:
        ingredient_words = ingredient.split()
        ingredient_lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos="n") for word in ingredient_words
        ]
        lemmatized.append("_".join(ingredient_lemmatized))
    return lemmatized


def preproc_ingredients(user_input):
    # preproces input same way as df

    # 1.lowercase
    user_input = [i.lower() for i in user_input]

    # 2. remove numbers

    user_input = [remove_num(i) for i in user_input]

    # 3. remove spaces

    user_input = [i.strip() for i in user_input]

    # 4. remove special chars

    user_input = remove_punctuation(user_input)

    # 5. lemmatize and join words with underscores

    user_input = lemmatize_ingredients(user_input)

    # 6. change to set

    user_input = set(user_input)

    return user_input
