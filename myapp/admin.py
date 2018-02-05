# -*- coding: utf-8 -*-

from django.contrib import admin
from myapp.models.blog import Post, Comment
from myapp.models.core import UserProfile
from myapp.models.music_band import Person, Group, Membership


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


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_all_members')
    list_filter = ['name']
    search_fields = ['name']


class MembershipAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Membership information', {
            'fields': [
                'person', 'group', 'invite_reason', 'date_joined', 'actived'
            ]
        }),
    ]
    list_display = ('invite_reason', 'date_joined', 'actived')
    list_filter = ['date_joined']
    search_fields = ['invite_reason']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
