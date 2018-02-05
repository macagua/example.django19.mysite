# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from survey.models import Survey
from survey.serializers import SurveySerializer


class SurveyList(APIView):
    '''
    List all surveys, or create a new survey
    '''
    def get(self, request, format=None):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyDetail(APIView):
    '''
    Get, update, or delete a specific survey
    '''
    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
