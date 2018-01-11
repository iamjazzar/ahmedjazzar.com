from urllib import parse

from django.conf import settings
from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


class Blog(models.Model):
    slug = models.SlugField(unique=True)

    title = models.CharField(max_length=128)
    text = models.TextField()

    short_description = models.CharField(max_length=160)
    image = models.ImageField(upload_to='blog', null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def email_share_url(self):
        subject = 'Join me reading this {} article'.format(self.title)

        body = 'I\'ve read Ahmed Jazzar\'s article! Join along for a ' \
               'delightful reading {}'.format(self.get_full_url()
        )

        return 'mailto:?subject={subject}&body={body}'.format(
            subject=subject, body=body)

    @property
    def facebook_share_url(self):
        return 'https://www.facebook.com/sharer.php?u={}'.format(
            parse.quote(self.get_full_url()))

    @property
    def twitter_share_url(self):
        text = 'I\'ve read #AhmedJazzar\'s article! Join along for a ' \
               'delightful reading {}'.format(self.get_full_url())

        return 'https://www.twitter.com/intent/tweet?text={}'.format(
            parse.quote(text))

    def get_full_url(self):
        object_path = reverse('post', kwargs={'slug': self.slug})
        full_url = parse.urljoin(settings.SITE_BASE, object_path)

        return full_url

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(**kwargs)

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True, null=True)

    resolved = models.BooleanField(default=False)


class ImageModel(models.Model):
    image = models.ImageField(upload_to='work')


class SocialAccount(models.Model):
    name = models.CharField(max_length=55)
    link = models.URLField()
    css_class = models.CharField(max_length=128, null=True, blank=True)

    def get_class(self):
        alternative_class = 'fa-{}'.format(self.name.lower())
        return self.css_class or alternative_class


class Work(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=128, db_index=True)
    type = models.CharField(max_length=128)
    short_description = models.CharField(max_length=128)
    description = models.TextField()
    services = models.CharField( max_length=512)
    main_image = models.ImageField(upload_to='works')
    link = models.URLField(blank=True, null=True)

    images = models.ManyToManyField(ImageModel)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super(Work, self).save(**kwargs)

    def get_services_display(self):
        return self.services.split(';')