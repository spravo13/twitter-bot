#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from keys import keys

#filename stated after 'python tweet_from_list.py'
argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(status=line)
	time.sleep(600)#seconds
