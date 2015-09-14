from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import models

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        header = models.HeaderData.objects.get(pk=1)
        navs = models.Nav.objects.all()

        context['MEDIA_URL'] = settings.MEDIA_URL
        context['full_name'] = header.get_full_name()
        context['about'] = header.get_about()
        context['country'] = header.get_country()
        context['country_image'] = header.get_country_image()
        context['logo'] = header.get_logo()
        context['navs'] = navs

        return context
