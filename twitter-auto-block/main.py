import tweepy
from time import sleep
from re import search
from config import *
from itertools import cycle
from random import shuffle

# authorization from values inputted earlier, do not change.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def get_friends():
    # gets a list of your followers and following
    followers = api.get_follower_ids(screen_name=screen_name)
    following = api.get_friend_ids(screen_name=screen_name)

    return followers, following

def block_everyone(followers, following):
    total_blocked = 0

    # starts following users.
    for f in followers:
        try:
            api.create_block(user_id=f)
            total_blocked += 1
            print('Blocked user. Sleeping 20 seconds.' + str(total_blocked) + ' users blocked so far.')
            sleep(20)
        except (Exception) as e:
            error_handling(e)
    print(total_blocked)

def block_non_mutuals(followers, following):
    # Makes a list of  those you don't follow back.
    non_following = set(followers) - set(following)
    total_blocked = 0

    # starts following users.
    for f in non_following:
        try:
            api.create_block(user_id=f)
            total_blocked += 1
            print('Blocked user. Sleeping 20 seconds.' + str(total_blocked) + ' users blocked so far.')
            sleep(20)
        except (Exception) as e:
            error_handling(e)
    print(total_blocked)

# function to handle errors
def error_handling(e):
    print(e)

action = input("Press 1 to block everyone, press 2 to block non-mutuals.")

if (int(action == 1)):
    block_everyone(*get_friends())
elif (int(action) == 2):
    block_non_mutuals(*get_friends())