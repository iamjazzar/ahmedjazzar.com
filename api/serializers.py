"""
Serializers define the API representation.
"""

from rest_framework import serializers

from ahmedjazzarcom.models import Blog, Work


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'slug',
            'title',
            'text',
            'short_description',
            'image',
            'featured',
            'pub_date',
        )


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = (
            'slug',
            'name',
            'type',
            'short_description',
            'description',
            'services',
            'link',
        )
