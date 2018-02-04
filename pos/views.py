# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import renderers
from rest_framework.decorators import detail_route
from pos.api.pagination import LimitTenPagination
from pos.api.permissions import IsOwnerOrReadOnly
from pos.models import UserProfile, PointOfSale
from pos.serializers import UserSerializer, UserProfileSerializer, PointOfSaleSerializer


def web_client(request):
    """
    Simple view for shows how consume our RESTful API from Javascript.
    """
    return render(request, 'pos/index.html')


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PointOfSaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Point of sale to be viewed or edited.
    """
    queryset = PointOfSale.objects.all().order_by('-name')
    serializer_class = PointOfSaleSerializer
