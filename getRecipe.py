import tweepy
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import settings

cred = credentials.Certificate("buzzrecipematome-firebase-adminsdk-h15r1-c07517e0f1.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

consumer_key = settings.CONSUMER_KEY 
consumer_secret = settings.CONSUMER_SECRET
access_token_key = settings.ACCESS_TOKEN_KEY
access_token_secret = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

statuses = api.list_timeline(slug='recipe', owner_screen_name='flowphantom')

docs = db.collection('recipe').stream() 
exists_tweet_list = list(map(lambda doc: doc.to_dict()['tweetLink'], docs))

for status in statuses:
    status = status._json
    # status = api.get_status(tweetID)._json
    try:
        if status['text'][0:2] == 'RT':
            continue
        url = 'https://twitter.com/' + status['user']['screen_name'] + '/status/' + status['id_str']

        if url in exists_tweet_list:
            continue
        # doc_ref.set({
        #     'tweetLink': url,
        #     'tweetText': status['text'],
        # })

        print(url)
        print(status['text'])
        print('------   ')
    except IndexError:
        pass
print(len(statuses))
