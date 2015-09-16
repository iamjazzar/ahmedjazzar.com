
from django.conf import settings

from twitter import *
import re

# TODO: rewrite functions into classes
# TODO: return marked down results

def get_tweet():
    auth = OAuth(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        token=settings.ACCESS_TOKEN,
        token_secret=settings.ACCESS_TOKEN_SECRET,
    )

    tweets = Twitter(auth=auth).statuses.user_timeline(screen_name=settings.TWITTER_USERNAME)

    return tweets[0].get('text')

def get_tweet_date():
    auth = OAuth(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        token=settings.ACCESS_TOKEN,
        token_secret=settings.ACCESS_TOKEN_SECRET,
    )

    tweets = Twitter(auth=auth).statuses.user_timeline(screen_name=settings.TWITTER_USERNAME)

    return tweets[0].get('created_at')[0:10]
