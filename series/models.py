# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Serie(models.Model):

    HORROR = 'horror'
    FICTION = 'fiction'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (FICTION, 'Fiction'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.name
