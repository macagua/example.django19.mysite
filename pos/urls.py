# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from pos import views

router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'list', views.PointOfSaleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^web-client/$', views.web_client, name='web-client'),
]
