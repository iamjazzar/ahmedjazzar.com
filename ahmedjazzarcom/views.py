
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

from helpers import last_tweet
import models


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        try:
            header = models.HeaderData.objects.get(pk=1)
            full_name = header.get_full_name()
            about = header.get_about()
            country = header.get_country()
            country_image = header.get_country_image()
            logo = header.get_logo()

            navs = models.Nav.objects.all()

        except:
             full_name = "Full Name"
             about = "Wow! I can see you now :D"
             country = "Country"
             country_image = None
             logo = None

             navs = None


        tweet = last_tweet()

        context['MEDIA_URL'] = settings.MEDIA_URL
        context['full_name'] = full_name
        context['about'] = about
        context['country'] = country
        context['country_image'] = country_image
        context['logo'] =  logo
        context['navs'] = navs
        context['tweet'] = tweet.get('tweet')
        context['tweet_date'] = tweet.get('time')
        context['TWITTER_USERNAME'] = settings.TWITTER_USERNAME
        context['GITHUB_USERNAME'] = settings.GITHUB_USERNAME
        context['FACEBOOK_USERNAME'] = settings.FACEBOOK_USERNAME
        context['EMAIL'] = settings.EMAIL

        return context
