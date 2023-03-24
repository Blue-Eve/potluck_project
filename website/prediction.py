import joblib
from matplotlib.pyplot import clf
from potluck_code.logic import model


def predict(ingredients):
    clf = model.easy_search(ingredients, 3)
    return clf

# testing the predict function
if __name__=='__main__':
    print(predict(['water', 'salt', 'tomatoes']))
