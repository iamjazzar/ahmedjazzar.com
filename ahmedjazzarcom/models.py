import os
from django.db import models
from django.conf import settings

from datetime import date

class MainPage(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='images') # TODO: Optimize before save
    country = models.CharField(max_length=15)
    work_location = models.CharField(max_length=25)
    organization = models.CharField(max_length=25)
    position = models.CharField(max_length=50)
    organization_link = models.CharField(max_length=100)
    email = models.EmailField()
    github_username = models.CharField(max_length=25)
    twitter_username = models.CharField(max_length=25)
    linkedin_username = models.CharField(max_length=25)
    facebook_username = models.CharField(max_length=25)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_full_name(self):
        return '{} {}'.format(self.first_name.capitalize(), self.last_name.capitalize())

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_logo(self):
        return self.logo

    def get_country(self):
        return self.country

    def get_work_location(self):
        return self.work_location

    def get_organization(self):
        return self.organization

    def get_organization_link(self):
        return self.organization_link

    def get_position(self):
        return self.position

    def get_email(self):
        return self.email

    def get_github_username(self):
        return self.github_username

    def get_twitter_username(self):
        return self.twitter_username

    def get_linkedin_username(self):
        return self.linkedin_username

    def get_facebook_username(self):
        return self.facebook_username

    def __unicode__(self):
        return self.get_full_name()

class Interest(models.Model):
    interest  = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.interest

class LatestProject(models.Model):

    project = models.CharField(max_length=30)
    url = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.project


class SideBar(models.Model):
    about = models.TextField()
    birth_date = models.DateField()
    interests = models.ManyToManyField(Interest)
    latest_projects = models.ManyToManyField(LatestProject)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_about(self):
        return self.about

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def get_interests(self):
        return self.interests.all()

    def get_latest_projects(self):
        return self.latest_projects.all()

    def __unicode__(self):
        return self.about
