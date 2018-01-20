from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import RedirectView

from ahmedjazzarcom import views
from ahmedjazzarcom.sitemaps import sitemaps


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('api/upload/', views.MarkdownUploader.as_view(),
         name='markdown_uploader_page'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.BlogPostView.as_view(), name='post'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('works', views.WorksView.as_view(), name='works'),
    path('work/<slug:slug>', views.WorkView.as_view(), name='work'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt', include('robots.urls', )),

    # Includes
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),

    # Old patterns
    path('single-post/<slug:slug>',
         RedirectView.as_view(pattern_name='post')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
