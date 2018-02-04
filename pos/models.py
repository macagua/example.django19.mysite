# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

 
class UserProfile(models.Model):
    """
    Represent the User Profile, where the user will update your information
    """
    user = models.OneToOneField(User, related_name='user')
    photo = models.ImageField(upload_to='pos/static/images/avatars/',
        null=True, blank=True, verbose_name="Profile Picture")
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.user)


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

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def get_userprofiles(self):
        return self.userprofile.all()
