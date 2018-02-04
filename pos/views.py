# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets
from pos.models import PointOfSale
from pos.serializers import PointOfSaleSerializer


def web_client(request):
    """
    Simple view for shows how consume our RESTful API from Javascript.
    """
    return render(request, 'pos/index.html')


class PointOfSaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Point of sale to be viewed or edited.
    """
    queryset = PointOfSale.objects.all().order_by('-name')
    serializer_class = PointOfSaleSerializer
