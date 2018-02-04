# -*- coding: utf-8 -*-

from pos.api.pagination import LimitTenPagination
from pos.api.permissions import IsOwnerOrReadOnly

default_app_config = 'pos.apps.PosConfig'

"""
Source https://axiacore.com/blog/2012/06/introduccion-a-django-rest-framework/
"""