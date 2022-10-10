import tweepy
from time import sleep
from re import search
from config import *
from itertools import cycle
from random import shuffle
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def get_following():
    following = api.get_friend_ids(screen_name=screen_name)

    return following

def get_users(following):
    users = []
    count = 0
    for f in following:
        try:
            user = api.get_user(user_id=f)
            users.append(user._json)
            count += 1
            print('+1 user has been added to the list. ' + str(count) + ' users in the list.')
            
        except (Exception) as e:
            error_handling(e)
    return users

def error_handling(e):
    print(e)

user_data = json.dumps(get_users(get_following()))
with open('user_data.json', 'w') as outfile:
    outfile.write(user_data)

