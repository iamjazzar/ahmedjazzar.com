from django.db import models


class SocialAccount(models.Model):
    name = models.CharField(max_length=55)
    link = models.URLField()
    css_class = models.CharField(max_length=128, null=True, blank=True)

    def get_class(self):
        alternative_class = 'fa-{}'.format(self.name.lower())
        return self.css_class or alternative_class


class ContactRequest(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()

    resolved = models.BooleanField(default=False)
