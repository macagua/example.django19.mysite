# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from myapp.models.core import UserProfile

 
class PointOfSale(models.Model):
    """
    Represent the point of sale, where the customers will make reservation
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    brand = models.CharField(max_length=150, null=True,
        blank=True, help_text="Enter the brand of point of sale")
    longitude = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    options = models.TextField(default="")
    userprofile = models.ManyToManyField(UserProfile, related_name='user_profile',
        blank=True, help_text="Select the user profile")
    message = models.CharField(max_length=140, default="")
    actived = models.BooleanField(default=True,
        help_text="This point of sale is actived?")

    class Meta:
        verbose_name = "Point Of Sale"
        verbose_name_plural = "Points Of Sale"

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def get_userprofiles(self):
        return self.userprofile.all()
