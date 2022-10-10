import tweepy
import sys

auth = tweepy.OAuthHandler("XXXXXXXXXXXXX", "XXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXX")

api = tweepy.API(auth)

count = len(sys.argv)
query = sys.argv[1]
global exists
exists = False

public_tweets = api.home_timeline(tweet_mode="extended")
if (count == 2):
	for tweet in public_tweets:
		text = tweet._json['full_text']
		if (query in text):
			exists = True
			print(text)
			print("------------------------------------------------")

	if (not exists):
		print("No results were found")
elif count == 3:
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=sys.argv[2], tweet_mode="extended").items():
		text = tweet._json['full_text']
		if (query in text):
			exists = True
			print(text)
			print("------------------------------------------------")
	if (not exists):
		print("No results were found")