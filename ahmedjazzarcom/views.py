from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from ahmedjazzarcom import models


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['social_accounts'] = models.SocialAccount.objects.all()

        return context

    def post(self, request, **kwargs):
        data = request.POST
        name = data['name']
        email = data['email']
        message = data['message']

        models.ContactRequest.objects.create(
            name=name, email=email, message=message)

        return redirect(reverse('home'))
