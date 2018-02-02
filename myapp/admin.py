# -*- coding: utf-8 -*-

from django.contrib import admin
from myapp.models.music_band import Person, Group, Membership

# Register your models here.
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


admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
