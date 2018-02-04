# -*- coding: utf-8 -*-

from rest_framework import serializers
from webflix.models import TvSerie


class TvSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvSerie
        fields = ('id', 'name', 'release_date', 'rating', 'category')
