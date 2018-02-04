# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from pos.models import UserProfile, PointOfSale


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail',
                                               lookup_field='profile')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'url')


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


class PointOfSaleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializers for model PointOfSale
    """
    class Meta:
        model = PointOfSale
        fields = ('id', 'name', 'address', 'brand', 'longitude', 'latitude', 'options', 'userprofile', 'message', 'actived')
        ordering = ('-id',)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
