# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers
from polls import views
from polls.viewsets import QuestionViewSet, ChoiceViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

app_name = 'polls'
urlpatterns = [
    url(r'^', include(router.urls)),
    # ex: /polls/list/
    url(r'^list/$', views.list, name='list'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
