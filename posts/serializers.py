from posts.models import NavItem
from rest_framework import serializers


class NavItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavItem
        fields = ('id', 'title', 'link')
