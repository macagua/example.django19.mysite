# -*- coding: utf-8 -*-

from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')
        ordering = ('-id',)

    # def create(self, validated_data):
    #     pass

    # def update(self, instance, validated_data):
    #     pass


# class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
class ChoiceSerializer(serializers.ModelSerializer):
    """
    Serializers for model Choice
    """
    class Meta:
        model = Choice
        fields = "__all__"
        ordering = ('-id',)
