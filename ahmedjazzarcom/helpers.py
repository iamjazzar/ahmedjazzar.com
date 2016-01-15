
from django.conf import settings

from dateutil import parser
from datetime import datetime

from twitter import *


def last_tweets(twitter_user):
    auth = OAuth(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        token=settings.ACCESS_TOKEN,
        token_secret=settings.ACCESS_TOKEN_SECRET,
    )

    last_tweets=[]

    try:
        tweets_number = settings.TWEETS_NUMBER
        tweets = Twitter(auth=auth).statuses.user_timeline(screen_name=twitter_user)
        last_tweets=[(tweets[i].get('text'), parser.parse(tweets[i].get('created_at'))) for i in range(0, tweets_number)]
    except TwitterHTTPError:
        tweet = "OMG! You do not configure your Twitter account yet!"
        created_at = datetime.now()
        last_tweets=[(tweet, created_at)]
    except URLError:
        tweet = "OMG! Something went wrong, refereshing the page may solve the issue!"
        created_at = datetime.now()
        last_tweets=[(tweet, created_at)]

    return last_tweets
