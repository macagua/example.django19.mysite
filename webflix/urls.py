# -*- coding: utf-8 -*-

from django.conf.urls import url
from webflix import views


urlpatterns = [
    url(r'^tv-series/list/$', views.tv_serie_list),
    url(r'^tv-series/detail/(?P<pk>[0-9]+)/$', views.tv_serie_detail),
]
