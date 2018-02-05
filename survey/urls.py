# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from survey import views


urlpatterns = [
    url(r'^list/$', views.SurveyList.as_view(), name='survey_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.SurveyDetail.as_view(), name='survey_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
