import tweepy
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import os
from bs4 import BeautifulSoup
import requests
import re

# CookPadからぶっこ抜く
def getMaterials(event, context):
    recipe_id_list = context
    base_url = 'https://cookpad.com/recipe/'
    for recipe_id in recipe_id_list:
        r = requests.get(base_url + str(recipe_id))
        soup = BeautifulSoup(r.text, 'lxml')
        ingredients = soup.find_all('div', class_='ingredient_name')
        f = open('material_dictionary.txt', 'a', encoding='utf-8')
        for ingredient in ingredients:
            # 記号文字を抜きたい
            material = re.sub("[^ぁ-んァ-ンーa-zA-Z0-9一-龠０-９\-\r]", '', ingredient.text)
            f.write(material + '\n')
        f.close()

def getRecipeUrlFromCategoryPage(category_id):
    target_url = 'https://cookpad.com/category/' + str(category_id)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    # recipes = soup.find_all('a', href=re.compile("*/recipe/d{7}"))
    recipes = soup.find_all('a', href=re.compile("/recipe/\d{7}"))
    recipe_id_list = list(map(lambda recipe: re.search("\d{7}", recipe['href']).group(), recipes))
    getMaterials('hoge', recipe_id_list)

def getCategoryId():
    target_url = 'https://cookpad.com/category/list'
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    sub_category = soup.find_all('a', href=re.compile("/category/\d+"))
    category_id_list = list(map(lambda category: re.search("\d+", category['href']).group(), sub_category))
    category_id_list = list(set(category_id_list))
    for category_id in category_id_list:
        getRecipeUrlFromCategoryPage(category_id)


if __name__ == '__main__':
    getCategoryId()