# -*- coding: utf-8 -*-

from django.conf.urls import include, url 
from rest_framework.urlpatterns import format_suffix_patterns 
from myapp import viewsets


post_list = viewsets.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = viewsets.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_creation = viewsets.PostViewSet.as_view({
    'post': 'set_comment'
})


urlpatterns = [
   url(r'^v1/posts/$', post_list, name='post_list'), 
   url(r'^v1/post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'), 
   url(r'^v1/post/(?P<pk>[0-9]+)/comment/$', comment_creation, name='comment_creation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)