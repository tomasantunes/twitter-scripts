import tweepy
import sys
import win32com.client as wincl


auth = tweepy.OAuthHandler("XXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXX")

api = tweepy.API(auth)

count = len(sys.argv)
global exists
exists = False

speak = wincl.Dispatch("SAPI.SpVoice")

def cleanTweet(text):
	stopwords = ('http','rt','@', '#')
	textwords = text.split(" ")

	resultwords  = [word for word in textwords if not word.lower().startswith(stopwords)]
	result = ' '.join(resultwords)
	return result


public_tweets = api.home_timeline(tweet_mode='extended')
if (count == 1):
	for tweet in public_tweets:
		text = tweet._json['full_text']
		text = cleanTweet(text)
		exists = True
		print(text)
		print("------------------------------------------------")
		speak.Speak(text)
	if (not exists):
		print("No results were found")
elif count == 2:
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=sys.argv[1], tweet_mode="extended").items():
		text = tweet.full_text.encode("utf8")
		text = cleanTweet(text)
		exists = True
		print(text)
		print("------------------------------------------------")
		speak.Speak(text)
		
	if (not exists):
		print("No results were found")