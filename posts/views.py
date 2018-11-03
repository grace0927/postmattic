from posts.models import NavItem
from rest_framework import viewsets
from posts.serializers import NavItemSerializer


class NavItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nav item to be viewed or edited.
    """
    queryset = NavItem.objects.all()
    serializer_class = NavItemSerializer
