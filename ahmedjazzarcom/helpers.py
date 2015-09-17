
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

    tweets = Twitter(auth=auth).statuses.user_timeline(screen_name=settings.TWITTER_USERNAME)
    last_tweet = {
        'tweet': tweets[0].get('text'),
        'time': pretty_date(parser.parse(tweets[0].get('created_at'))),
    }

    return last_tweet

def pretty_date(time=False):

    diff = datetime.now() - time.replace(tzinfo=None)

    seconds_diff = diff.seconds
    days_diff = diff.days

    if days_diff == 0:
        if seconds_diff < 10:
            return "just now"
        if seconds_diff < 60:
            return str(seconds_diff) + " seconds ago"
        if seconds_diff < 120:
            return "a minute ago"
        if seconds_diff < 3600:
            return str(seconds_diff / 60) + " minutes ago"
        if seconds_diff < 7200:
            return "an hour ago"
        if seconds_diff < 86400:
            return str(seconds_diff / 3600) + " hours ago"
    if days_diff == 1:
        return "Yesterday"
    if days_diff < 7:
        return str(days_diff) + " days ago"
    if days_diff < 31:
        return str(days_diff / 7) + " weeks ago"
    if days_diff < 365:
        return str(days_diff / 30) + " months ago"
    return str(days_diff / 365) + " years ago"
