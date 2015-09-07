from django.contrib import admin

from models import HeaderData

class HeaderDataAdmin(admin.ModelAdmin):
    list_display=["pk", "__unicode__", "updated"]


admin.site.register(HeaderData, HeaderDataAdmin)
