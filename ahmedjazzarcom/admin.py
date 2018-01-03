from django.contrib import admin

from ahmedjazzarcom import models


class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resolved']
    readonly_fields = ('name', 'email', 'message')


admin.site.register(models.SocialAccount, SocialAccountAdmin)
admin.site.register(models.ContactRequest, ContactRequestAdmin)
