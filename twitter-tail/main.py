import tweepy
import sys
import time

auth = tweepy.OAuthHandler("XXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXX")

api = tweepy.API(auth)

count = len(sys.argv)
home_last_tweet = ""
user_last_tweet = ""

def get_home_tweet():
	global home_last_tweet
	tweet = api.home_timeline(tweet_mode="extended", count = 1)[0]._json['full_text']
	if tweet != home_last_tweet:
		home_last_tweet = tweet
		print(tweet)
		print("------------------------------------------------")
	time.sleep(20)
	get_home_tweet()

def get_user_tweet():
	global user_last_tweet
	tweet = api.user_timeline(screen_name=sys.argv[1], tweet_mode="extended", count = 1)[0]._json['full_text']
	if tweet != user_last_tweet:
		user_last_tweet = tweet
		print(tweet)
		print("------------------------------------------------")
	time.sleep(20)
	get_user_tweet()
	
	

if count == 1:
	get_home_tweet()
elif count == 2:
	get_user_tweet()
