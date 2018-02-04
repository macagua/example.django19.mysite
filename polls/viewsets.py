# -*- coding: utf-8 -*-

from rest_framework import viewsets
from polls.models import Choice, Question
from polls.serializers import ChoiceSerializer, QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Question to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choice to be viewed or edited.
    """
    queryset = Choice.objects.all().order_by('-id')
    serializer_class = ChoiceSerializer
