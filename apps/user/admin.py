from django.contrib import admin
from .models import *



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')

admin.site.register(User, UserAdmin)