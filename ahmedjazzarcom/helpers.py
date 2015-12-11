
from django.conf import settings

from dateutil import parser
from datetime import datetime

from twitter import *


def last_tweet():
    auth = OAuth(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        token=settings.ACCESS_TOKEN,
        token_secret=settings.ACCESS_TOKEN_SECRET,
    )

    try:
        tweets = Twitter(auth=auth).statuses.user_timeline(screen_name=settings.TWITTER_USERNAME)
        tweet = tweets[0].get('text')
        created_at = parser.parse(tweets[0].get('created_at'))
    except TwitterHTTPError:
        tweet = "OMG! You do not configure your Twitter account yet!"
        created_at = datetime.now()

    last_tweet = {
        'tweet': tweet,
        'time': created_at,
    }

    return last_tweet
