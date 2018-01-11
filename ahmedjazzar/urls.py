from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from ahmedjazzarcom import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.BlogPostView.as_view(), name='post'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('works', views.WorksView.as_view(), name='works'),
    path('work/<slug:slug>', views.WorkView.as_view(), name='work'),

    # Includes
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
