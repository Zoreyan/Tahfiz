from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='administrator-list'),
    path('create/', create, name='administrator-create'),
    path('delete/<int:pk>/', delete, name='administrator-delete'),
    path('details/<int:pk>/', details, name='administrator-details'),
]