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

verbs = open('verbs.txt').read()
verbs = re.findall(r'\w+', verbs)

adjective = open('adjectives.txt').read()
adjective = re.findall(r'\w+', adjective)


def chooseNoun():
    mainWord = random.choice(words)
    return mainWord


def chooseVerb():
    mainWord = random.choice(verbs)
    return mainWord


def chooseAdj():
    mainWord = random.choice(adjective)
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


def goViralOnTwitter():
    print(adjective1 + ' ' + noun1 + 's who ' + verb + ' ' + noun2 + 's are ' + adjective2)


for i in range(500):
    # Choose random words
    noun1 = chooseNoun()
    noun2 = chooseNoun()
    adjective1 = chooseAdj()
    adjective2 = chooseAdj()
    verb = chooseVerb()

    # Churn out 500 viral tweets babyyyyyyyyy
    goViralOnTwitter()


api.update_status(status=adjective1 + ' ' + noun1 + 's who ' + verb + ' ' + noun2 + 's are ' + adjective2)
