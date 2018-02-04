# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Serie


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')
