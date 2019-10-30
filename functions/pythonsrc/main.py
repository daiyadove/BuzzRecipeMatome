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

def getRecipeTweet(event, context):

    # cred = credentials.Certificate("buzzrecipematome-firebase-adminsdk-h15r1-c07517e0f1.json")
    # firebase_admin.initialize_app(cred)
    # Use the application default credentials
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(cred, {
    #   'projectId': 'buzzrecipematome',
    # })
    if (not len(firebase_admin._apps)):
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'buzzrecipematome',
        })

    db = firestore.client()

    # consumer_key = settings.CONSUMER_KEY 
    # consumer_secret = settings.CONSUMER_SECRET
    # access_token_key = settings.ACCESS_TOKEN_KEY
    # access_token_secret = settings.ACCESS_TOKEN_SECRET

    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token_key = os.getenv('ACCESS_TOKEN_KEY')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    statuses = api.list_timeline(slug='recipe', owner_screen_name='flowphantom')

    docs = db.collection('recipe').stream() 
    exists_tweet_list = list(map(lambda doc: doc.to_dict()['tweetLink'], docs))

    recipe_words = [
        'フライパン',
        '電子レンジ',
        '500W',
        '600W'
    ]

    doc_ref = db.collection('recipe').document()

    for status in statuses:
        status = status._json
        # status = api.get_status(tweetID)._json
        try:
            if status['text'][0:2] == 'RT':
                continue
            url = 'https://twitter.com/' + status['user']['screen_name'] + '/status/' + status['id_str']

            # 既レシピは追加しない
            if url in exists_tweet_list:
                continue

            # レシピワードが含まれているか検査する
            has_recie_word = any(list(map(lambda recipe_word: recipe_word in status['text'], recipe_words)))
            # レシピワードがないツイートは追加しない
            if not(has_recie_word):
                continue

            doc_ref.set({
                'tweetLink': url,
                'tweetText': status['text'],
            })

            print(url)
            print(status['text'])
            print('------   ')
            time.sleep(2)
        except IndexError:
            pass

# CookPadからぶっこ抜く
def getMaterials(event, context):
    recipe_id_list = context
    base_url = 'https://cookpad.com/recipe/'
    for recipe_id in recipe_id_list:
        r = requests.get(base_url + str(recipe_id))
        soup = BeautifulSoup(r.text, 'lxml')
        ingredients = soup.find_all('div', class_='ingredient_name')
        kigou = []
        for ingredient in ingredients:
            # 記号文字を抜きたい
            material = re.sub("[^ぁ-んァ-ンーa-zA-Z0-9一-龠０-９\-\r]", '', ingredient.text)
            print(material)

def getRecipeUrl():
    target_url = 'https://cookpad.com/category/10'
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
    print(list(set(category_id_list)))

if __name__ == "__main__":
    # getMaterials('hoge', 'fuga')
    # getRecipeUrl()
    getCategoryId()

    