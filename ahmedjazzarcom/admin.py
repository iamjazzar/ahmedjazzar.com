from django.contrib import admin
from django.db import models as django_models

from martor.widgets import AdminMartorWidget

from ahmedjazzarcom import models


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['coffee_cups', 'clients', 'projects', 'hours', ]


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'featured']
    formfield_overrides = {
        django_models.TextField: {'widget': AdminMartorWidget},
    }


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resolved']
    readonly_fields = ('name', 'email', 'message', )


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['page', 'header']


class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


admin.site.register(models.AboutMe, AboutMeAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.ContactRequest, ContactRequestAdmin)
admin.site.register(models.ImageModel, ImageAdmin)
admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.SocialAccount, SocialAccountAdmin)
admin.site.register(models.Work, WorkAdmin)
