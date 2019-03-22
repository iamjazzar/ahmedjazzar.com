"""
ViewSets define the view behavior.
"""
from rest_framework import viewsets

from ahmedjazzarcom.models import Blog, Work
from api.serializers import BlogSerializer, WorkSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.get_ready()
    serializer_class = BlogSerializer
    lookup_field = 'slug'


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    lookup_field = 'slug'
