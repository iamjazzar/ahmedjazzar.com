from django.contrib import admin

import models

class HeaderDataAdmin(admin.ModelAdmin):
    list_display=["pk", "__unicode__", "updated"]

class NavAdmin(admin.ModelAdmin):
    list_display=["__unicode__", "updated"]

admin.site.register(models.HeaderData, HeaderDataAdmin)
admin.site.register(models.Nav, NavAdmin)
