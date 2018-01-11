from django.contrib import admin

from ahmedjazzarcom import models


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resolved']


class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    readonly_fields = ('slug', )


admin.site.register(models.ImageModel, ImageAdmin)
admin.site.register(models.SocialAccount, SocialAccountAdmin)
admin.site.register(models.ContactRequest, ContactRequestAdmin)
admin.site.register(models.Work, WorkAdmin)
