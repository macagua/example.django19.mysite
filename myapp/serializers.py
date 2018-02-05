# -*- coding: utf-8 -*-

from rest_framework import serializers
from myapp.models.blog import Post, Comment
from myapp.models.core import UserProfile
from mysite.serializers import UserProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'owner')


class PostSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, 
    	queryset=UserProfile.objects.all(), source='owner')
    comments = CommentSerializer(many=True, read_only=True, 
    	source='comment_set')

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'ownerId', 'comments')
