# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework import renderers
from rest_framework.decorators import detail_route
from myapp.models.core import UserProfile
from mysite.serializers import UserSerializer, UserProfileSerializer
# from pos.api.pagination import LimitTenPagination
from pos.api.permissions import IsOwnerOrReadOnly

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions
#     """
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
        IsOwnerOrReadOnly,)
    # pagination_class = LimitTenPagination

    @detail_route(renderer_classes=[renderers.JSONRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
