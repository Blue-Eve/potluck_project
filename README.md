# Le Wagon Final Project: Potluck

Potluck is a final project of the 9-week full-time data science bootcamp, created by Alex, Eva, Omar and Tim.
This repo is a fork of the original code.

## Motivation

The motivation of this project is creating a receipe-search site which returns recipes with the ingredients you have - or similar ones.

The similar ingredients are found with the Word2Vec Model using the most_similar function.

## Data & Model

We use the [Food.com data set](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) from Kaggle (RAW_recipes & RAW_interactions) and the pretrained Woord2Vec, resp. [Food2Vec @ChantalMP](https://github.com/ChantalMP/Exploiting-Food-Embeddings-for-Ingredient-Substitution)