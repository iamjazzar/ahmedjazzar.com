from django.contrib import admin

import models

class MainPageAdmin(admin.ModelAdmin):
    list_display=["__unicode__", "pk", "updated"]

class SideBarAdmin(admin.ModelAdmin):
    list_display=["__unicode__", "updated"]

class InterestAdmin(admin.ModelAdmin):
    list_display=["__unicode__", "updated"]

class LatestProjectAdmin(admin.ModelAdmin):
    list_display=["__unicode__", "updated"]

admin.site.register(models.MainPage, MainPageAdmin)
admin.site.register(models.SideBar, SideBarAdmin)
admin.site.register(models.LatestProject, LatestProjectAdmin)
admin.site.register(models.Interest, InterestAdmin)
