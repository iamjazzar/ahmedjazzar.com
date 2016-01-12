
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from ahmedjazzarcom.views import FourOhFourView

from ahmedjazzarcom import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^404/$', views.FourOhFourView.as_view(), name='404'),
    url(r'^500/$', views.FiveHundredView.as_view(), name='500'),
]

handler404 = FourOhFourView.get_rendered_view()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
