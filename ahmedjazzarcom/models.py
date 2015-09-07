import os
from django.db import models
from django.conf import settings

images_path = os.path.join("static", "images")

class HeaderData(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    about = models.TextField()
    country = models.CharField(max_length=15)
    country_image = models.ImageField(upload_to=images_path)
    logo = models.ImageField(upload_to=images_path)
    pattern = models.ImageField(upload_to=images_path)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_full_name(self):
        return '{} {}'.format(self.first_name.capitalize(), self.last_name.capitalize())

    def get_about(self):
        return self.about

    def get_country(self):
        return self.country

    def get_country_image(self):
        return self.country_image

    def get_logo(self):
        return self.logo

    def __unicode__(self):
        return self.get_full_name()

class Nav(models.Model):
    name = models.CharField(max_length=15)
    href = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_name(self):
        return self.name

    def get_href(self):
        return self.href

    def __unicode__(self):
        return self.name
