from django.contrib import admin
from .models import *



class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

admin.site.register(Student, StudentAdmin)