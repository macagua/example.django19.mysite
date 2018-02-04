# -*- coding: utf-8 -*-

from django.conf.urls import url
from series import views


urlpatterns = [
    url(r'^list/$', views.serie_list),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.serie_detail),
]
