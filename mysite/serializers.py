# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myapp.models.core import UserProfile


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializers for model UserProfile
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = "__all__"
        ordering = ('-username',)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
