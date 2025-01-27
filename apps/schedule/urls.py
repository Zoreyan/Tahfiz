from django.urls import path
from .views import *


urlpatterns = [
    path('', schedule, name='schedule'),
    path('delete/<int:pk>/', delete, name='schedule-delete'),
    path('subjects/', subject_create, name='subject-create'),
    path('create/', create, name='schedule-create'),
]