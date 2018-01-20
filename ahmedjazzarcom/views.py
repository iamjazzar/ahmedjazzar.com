import uuid

import os
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from meta.views import MetadataMixin

from secretballot.models import Vote

from ahmedjazzarcom import models


class JazzarMetadataMixin(MetadataMixin):
    description = _('I\'m Ahmed Jazzar, a 23 years old senior '
                    'software engineer working at Edraak on '
                    'creating Educational Tecnology.')
    keywords = [
        'Ahmed', 'Jazzar', 'Ahmad', 'Jazzar', 'Software', 'Engineer']
    url = settings.META_SITE_DOMAIN

    image = static('images/logo-grey.png')
    site_name = _('Ahmed Jazzar')
    twitter_site = 'https://www.twitter.com/iamjazzar'
    twitter_creator = 'iamjazzar'


class AboutView(JazzarMetadataMixin, TemplateView):
    description = _('About me, Ahmed Jazzar, the Software Engineer!')
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        context['tab'] = 'about'
        context['sliders'] = models.Slider.for_page(page='about')

        return context


class BlogView(MetadataMixin, ListView):
    description = _('Ahmed Jazzar\'s blog!')
    queryset = models.Blog.get_ready()
    template_name = 'blog.html'


    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)

        context['tab'] = 'blog'
        context['sliders'] = models.Slider.for_page(page='blog')

        return context


@method_decorator(csrf_exempt, name='dispatch')
class BlogPostView(DetailView):
    template_name = 'blog_post.html'
    model = models.Blog

    def get(self, *args, **kwargs):
        self.count_view()
        return super(BlogPostView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)

        post = self.get_object()
        context['voted'] = self.did_vote(post=post)
        context['meta'] = post.as_meta(self.request)
        context['tab'] = 'blog'

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        voted = self.did_vote(post=post)

        if voted:
            return JsonResponse({'state': 'Already voted'}, status=406)

        token = request.secretballot_token
        post.add_vote(token=token, vote='+1')

        return JsonResponse({'state': 'Successfully voted'}, status=200)

    def count_view(self):
        obj, created = models.BlogView.objects.get_or_create(
            blog=self.get_object())

        token = self.request.secretballot_token
        obj.add_vote(token=token, vote='+1')

    def did_vote(self, post):
        content_type = ContentType.objects.get_for_model(self.model).id
        token = self.request.secretballot_token

        return Vote.objects.filter(
            object_id=post.id,
            content_type=content_type,
            token=token).exists()


class ContactView(MetadataMixin, TemplateView):
    template_name = 'contact.html'
    description = _('Contact me, Ahmed Jazzar!')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        context['tab'] = 'contact'
        context['sliders'] = models.Slider.for_page('contact')

        return context

    def post(self, request, **kwargs):
        data = request.POST
        name = data['name']
        email = data['email']
        message = data['message']

        if message and email:
            models.ContactRequest.objects.create(
                name=name, email=email, message=message)

        return redirect(reverse('home'))


class HomeView(MetadataMixin, TemplateView):
    description = _('I\'m Ahmed Jazzar, a 23 years old senior '
                    'software engineer working at Edraak on '
                    'creating Educational Tecnology.')
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['tab'] = 'home'
        context['works'] = models.Work.objects.order_by('-created')[:3]
        context['about'] = models.AboutMe.objects.last()
        context['sliders'] = models.Slider.for_page(page='home')
        context['featured'] = models.Blog.get_ready().filter(
            featured=True).last()

        return context


class WorksView(MetadataMixin, ListView):
    template_name = 'works.html'
    queryset = models.Work.objects.order_by('-created')
    description = _('Ahmed Jazzar\'s projects!')

    def get_context_data(self, **kwargs):
        context = super(WorksView, self).get_context_data(**kwargs)

        context['tab'] = 'work'
        context['sliders'] = models.Slider.for_page(page='work')

        return context


class WorkView(DetailView):
    template_name = 'work.html'
    model = models.Work

    def get_context_data(self, **kwargs):
        context = super(WorkView, self).get_context_data(**kwargs)

        context['tab'] = 'work'
        context['meta'] = self.get_object().as_meta(self.request)

        return context


@method_decorator(staff_member_required, name='dispatch')
class MarkdownUploader(View):
    supported_types = [
        'image/png',
        'image/jpg',
        'image/jpeg',
        'image/pjpeg',
        'image/gif',
    ]

    def post(self, request, *args, **kwargs):
        """
        Markdown image upload request
        """
        if request.is_ajax():
            if 'markdown-image-upload' in request.FILES:
                image = request.FILES['markdown-image-upload']

                if image.content_type not in self.supported_types:
                    data = {
                        'status': 405, 'error': _('Bad image format.')
                    }

                    return JsonResponse(data, status=405)

                max_size = settings.MAX_IMAGE_UPLOAD_SIZE
                if image._size > max_size:
                    size = max_size / (1024*1024)
                    error_msg = _('Maximum image file is {size} MB.')

                    data = {
                        'status': 405,
                        'error': error_msg.format(size)
                    }

                    return JsonResponse(data, status=405)

                img_uuid = "{0}-{1}".format(
                    uuid.uuid4().hex[:10],
                    image.name.replace(' ', '-')
                )

                tmp_file = os.path.join(
                    settings.MARTOR_UPLOAD_PATH, img_uuid)

                def_path = default_storage.save(
                    tmp_file, ContentFile(image.read()))

                img_url = os.path.join(settings.MEDIA_URL, def_path)

                data = {
                    'status': 200, 'link': img_url, 'name': image.name
                }
                return JsonResponse(data)

            data = {
                'status': 405,
                'error': _('Invalid request!')
            }
            return JsonResponse(data, status=405)

        data = {
            'status': 405, 'error': _('Invalid request!')
        }

        return JsonResponse(data, status=405)
