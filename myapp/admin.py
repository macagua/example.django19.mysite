# -*- coding: utf-8 -*-

from django.contrib import admin
from myapp.models.blog import Post, Comment
from myapp.models.core import UserProfile


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3
    list_display = ('owner', 'title', 'body')
    list_filter = ['owner']
    search_fields = ['title', 'body']


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


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


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile, UserProfileAdmin)
