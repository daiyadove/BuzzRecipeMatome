import tweepy
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import settings
import os

def getRecipeTweet():

    cred = credentials.Certificate("buzzrecipematome-firebase-adminsdk-h15r1-c07517e0f1.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    consumer_key = settings.CONSUMER_KEY 
    consumer_secret = settings.CONSUMER_SECRET
    access_token_key = settings.ACCESS_TOKEN_KEY
    access_token_secret = settings.ACCESS_TOKEN_SECRET

    # consumer_key = os.getenv('CONSUMER_KEY')
    # consumer_secret = os.getenv('CONSUMER_SECRET')
    # access_token_key = os.getenv('ACCESS_TOKEN_KEY')
    # access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

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

            # doc_ref.set({
            #     'tweetLink': url,
            #     'tweetText': status['text'],
            # })

            print(url)
            print(status['text'])
            print('------   ')
            time.sleep(2)
        except IndexError:
            pass

if __name__ == '__main__':
    getRecipeTweet()