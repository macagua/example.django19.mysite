# -*- coding: utf-8 -*-

from rest_framework import serializers
from survey.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'owner', 'title','question', 'active', 'created', 'updated')
