from django.db import models
from django.utils.text import slugify


class SocialAccount(models.Model):
    name = models.CharField(max_length=55)
    link = models.URLField()
    css_class = models.CharField(max_length=128, null=True, blank=True)

    def get_class(self):
        alternative_class = 'icon-{}'.format(self.name.lower())
        return self.css_class or alternative_class


class ContactRequest(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()

    resolved = models.BooleanField(default=False)


class ImageModel(models.Model):
    image = models.ImageField(upload_to='work')


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