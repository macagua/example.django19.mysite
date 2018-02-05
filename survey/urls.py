# -*- coding: utf-8 -*-

from django.conf.urls import url
from survey import views


urlpatterns = [
    url(r'^list/$', views.survey_list, name='survey_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.survey_detail, name='survey_detail'),
]
