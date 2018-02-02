# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __unicode__(self):
        return "%s" % (self.name)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __unicode__(self):
        return "%s" % (self.name)

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    actived = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __unicode__(self):
    	date_joined = self.date_joined.isoformat().replace('', '')
        return "Member: %s from %s" % (self.actived, date_joined)
