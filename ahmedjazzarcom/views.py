from django.shortcuts import render
from django.views.generic import TemplateView

from models import HeaderData

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        header = HeaderData.objects.get(pk=1)

        context['full_name'] = header.get_full_name()
        context['about'] = header.get_about()
        context['country'] = header.get_country()
        context['country_image'] = header.get_country_image()
        context['logo'] = header.get_logo()

        return context
