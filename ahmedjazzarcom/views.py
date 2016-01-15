
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

from helpers import last_tweets
import models

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        main = models.MainPage.objects.get(pk=1)

        first_name = main.get_first_name()
        last_name = main.get_last_name()
        full_name = main.get_full_name()
        logo = main.get_logo()
        country = main.get_country()
        work_location = main.get_work_location()
        email = main.get_email()
        github_user = main.get_github_username()
        twitter_user = main.get_twitter_username()
        linkedin_user = main.get_linkedin_username()
        facebook_user = main.get_facebook_username()
        organization = main.get_organization()
        position = main.get_position()
        organization_link = main.get_organization_link()

        side_bar = models.SideBar.objects.all()[0]

        about = side_bar.get_about()
        age = side_bar.get_age()
        interests = side_bar.get_interests()
        latest_projects = side_bar.get_latest_projects()

        timeline = last_tweets(twitter_user)

        context['MEDIA_URL'] = settings.MEDIA_URL
        context['first_name'] = first_name
        context['last_name'] = last_name
        context['full_name'] = full_name
        context['country'] = country
        context['organization'] = organization
        context['position'] = position
        context['organization_link'] = organization_link
        context['work_location'] = work_location
        context['logo'] = logo
        context['email'] = email
        context['github_user'] = github_user
        context['twitter_user'] = twitter_user
        context['linkedin_user'] = linkedin_user
        context['facebook_user'] = facebook_user

        context['about'] = about
        context['age'] = age
        context['interests'] = interests
        context['latest_projects'] = latest_projects

        context['timeline']=timeline

        return context

class FiveHundredView(TemplateView):
    template_name = "500.html"

    def get_context_data(self, **kwargs):
        context = super(FiveHundredView, self).get_context_data(**kwargs)
        context['EMAIL'] = settings.EMAIL

        return context

class FourOhFourView(TemplateView):
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = super(FourOhFourView, self).get_context_data(**kwargs)

        try:
            navs = models.Nav.objects.all()
        except:
            navs = None

        context['navs'] = navs

        return context

    @classmethod
    def get_rendered_view(cls):
        as_view_fn = cls.as_view()

        def view_fn(request):
            response = as_view_fn(request)
            response.render()
            return response

        return view_fn
