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

class setDictionary():
    def __init__(self):
        self.materials = []
        self.cleansinged_materials = []
        self.dictionary_path = 'material_dictionary.txt'
        self.openDictionary()
    
    def openDictionary(self):
        f = open(self.dictionary_path, 'r', encoding='utf-8')
        self.materials = f.readlines()
        f.close()
    
    def cleansingDictionary(self):
        f = open(self.dictionary_path, 'w', encoding='utf-8')
        self.cleansinged_materials = list(set(self.materials))
        f.write('\n'.join(self.cleansinged_materials))
        f.close()
    
    def saveFireStore(self):
        cred = credentials.Certificate("../buzzrecipematome-firebase-adminsdk-h15r1-c07517e0f1.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('materials').document('dictionary').set({'materials':self.cleansinged_materials})


if __name__ == '__main__':
    set_dictionary = setDictionary()
    set_dictionary.cleansingDictionary()
    set_dictionary.saveFireStore()