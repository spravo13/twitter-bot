import tweepy
from twython import Twython, TwythonError
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

try:
	search_results = twitter.search(q='#hashtag', count=50)
except TwythonError as e:
	print e

for tweet in search_results['statuses']:
	user = tweet['user']['screen_name'].encode('utf-8')
	api.create_friendship(user)
