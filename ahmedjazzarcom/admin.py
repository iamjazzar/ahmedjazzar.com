from django.contrib import admin

from ahmedjazzarcom import models


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['coffee_cups', 'clients', 'projects', 'hours', ]


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured']


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resolved']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['page', 'header']


class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.AboutMe, AboutMeAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.ImageModel, ImageAdmin)
admin.site.register(models.SocialAccount, SocialAccountAdmin)
admin.site.register(models.ContactRequest, ContactRequestAdmin)
admin.site.register(models.Work, WorkAdmin)
