# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from survey.models import Survey
from survey.serializers import SurveySerializer


class SurveyMixin(object):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


# class SurveyList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
class SurveyList(SurveyMixin, ListCreateAPIView):
    '''
    List all surveys, or create a new survey
    '''
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class SurveyDetail(APIView):
class SurveyDetail(SurveyMixin, RetrieveUpdateDestroyAPIView):
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
