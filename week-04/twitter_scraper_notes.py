import jsonpickle
import tweepy
import pandas as pd

#imports the keys from the hidden python file
#may need to change the working directory

import os
#os.chdir('week-04')
from twitter_keys import api_key, api_secret

auth = tweepy.AppAuthHandler(api_key, api_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

tweet_count += len(new_tweets)
#same as tweet_count = tweet_count + len(new_tweets)

#twitter expects
def get_tweets(
    geo,
    out_file,
    search_term, = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
):
tweet_count = 0

while tweet_count < tweet_max:
    try:
        if (max_id <= 0):
            if (not since_id):
