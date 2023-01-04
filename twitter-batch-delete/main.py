import tweepy
import traceback
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def batch_delete(api):
	print(
		"You are about to delete all tweets from the account @%s."
		% api.verify_credentials().screen_name
	)
	print("Does this sound ok? There is no undo! Type yes to carry out this action.")
	do_delete = input("> ")
	if do_delete.lower() == "yes":
		for status in tweepy.Cursor(api.user_timeline).items():
			try:
				api.destroy_status(status.id)
				print("Deleted:", status.id)
			except Exception:
				traceback.print_exc()
				print("Failed to delete:", status.id)


print("Authenticated as: %s" % api.verify_credentials().screen_name)
batch_delete(api)
	