# -*- coding: utf-8 -*-

from django.contrib import admin
from survey.models import Survey


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'question', 'active', 'created', 'updated')
    list_filter = ['owner', 'created', 'active',]
    search_fields = ['title', 'question']

admin.site.register(Survey, SurveyAdmin)
