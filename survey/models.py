# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Survey(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    def __unicode__(self):
        return "%s" % (self.title)

    def __str__(self):
        return self.title