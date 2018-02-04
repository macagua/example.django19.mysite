# -*- coding: utf-8 -*-

from django.contrib import admin
from webflix.models import TvSerie


class TvSerieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {
            'fields': [
                'name', 'release_date', 'rating', 'category'
            ]
        }),
    ]
    list_display = ('name', 'release_date', 'rating', 'category')
    list_filter = ['rating', 'category']
    search_fields = ['name', 'category']


admin.site.register(TvSerie, TvSerieAdmin)
