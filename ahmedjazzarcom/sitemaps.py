from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from ahmedjazzarcom.models import Blog, Work


class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Blog.get_ready()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.url


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)


class WorkSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Work.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.url


sitemaps = {
    'blog': BlogSitemap,
    'static': StaticViewSitemap,
    'work': WorkSitemap,
}
