from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from ahmedjazzarcom import models


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, **kwargs):
        data = request.POST
        name = data['name']
        email = data['email']
        message = data['message']

        if message and email:
            models.ContactRequest.objects.create(
                name=name, email=email, message=message)

        return redirect(reverse('home'))


class WorksView(ListView):
    template_name = 'works.html'
    model = models.Work


class WorkView(DetailView):
    template_name = 'work.html'
    model = models.Work
