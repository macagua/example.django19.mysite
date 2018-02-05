# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from myapp.models.core import UserProfile


class Post(models.Model):
    owner = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comment(models.Model):
    owner = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text
