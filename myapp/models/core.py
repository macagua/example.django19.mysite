# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

 
class UserProfile(models.Model):
    """
    Represent the User Profile, where the user will update your information
    """
    user = models.OneToOneField(User, related_name='user')
    photo = models.ImageField(upload_to='myapp/static/images/avatars/',
        null=True, blank=True, verbose_name="Profile Picture")
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.user)
