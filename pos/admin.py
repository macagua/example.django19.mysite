# -*- coding: utf-8 -*-

from django.contrib import admin
from pos.models import PointOfSale, UserProfile


class PointOfSaleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {
            'fields': [
                'name', 'brand'
            ]
        }),
        ('Contact information', {
            'fields': [
                'address', 'longitude', 'latitude'
            ]
        }),
        ('Options information', {
            'fields': [
                'userprofile', 'options', 'message', 'actived'
            ]
        })
    ]
    list_display = ('name', 'address', 'actived')
    list_filter = ['brand', 'actived']
    search_fields = ['name', 'address', 'brand']


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {
            'fields': [
                'user', 'photo', 'bio', 'organization'
            ]
        }),
        ('Contact information', {
            'fields': [
                'website', 'phone', 'city', 'country'
            ]
        }),
    ]
    list_display = ('user', 'photo', 'organization', 'phone', 'city', 'country')
    list_filter = ['organization', 'city', 'country']
    search_fields = ['user', 'address', 'organization']


admin.site.register(PointOfSale, PointOfSaleAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
