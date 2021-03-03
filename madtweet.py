
import re, sys, random, time
from string import ascii_lowercase
import spotipy
import tweepy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import requests
import json
import time
import sys

# Importing text file as list
words = open('nounlist.txt').read()
words = re.findall(r'\w+', words)

def chooseNoun():
    for i in range(len(words)):
        mainWord = random.choice(words)
        

    return mainWord

# Twitter personal details
consumer_key = "pZP7kFlAFKpegNSDIr5sLqUcr"
consumer_secret = "KLiAeezYG70EKe9uKKEdBXFISC5sfXk4215L3n7PtQGSg341pd"
access_token = "1114306019134398464-lgWL8QFlHnxOjJ5X2GrQ72rgBI3LOk"
access_token_secret = "sPhDeWSWwLmwtk7JM960YDFu7uV63IO72Qq379byc3mOD"

# Authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Authenticate Twitter with token
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

chosenNoun = chooseNoun()

# Execute the tweet
api.update_status(status=chosenNoun)

