from django.contrib import admin

# Register your models here.
from myapp.models import Person, Group, Membership

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
