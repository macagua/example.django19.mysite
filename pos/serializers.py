# -*- coding: utf-8 -*-

from rest_framework import serializers
from pos.models import PointOfSale


class PointOfSaleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializers for model PointOfSale
    """
    class Meta:
        model = PointOfSale
        fields = ('id', 'name', 'address', 'brand', 'longitude', 'latitude',
            'options', 'userprofile', 'message', 'actived')
        ordering = ('-id',)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
