from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserBoard (admin.ModelAdmin) : 
    list_display = ['full_name','email']

admin.site.register(User, UserBoard)
admin.site.unregister(Group)