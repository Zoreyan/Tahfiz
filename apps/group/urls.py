from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='group-list'),
    path('create/', create, name='group-create'),
    path('details/<str:pk>/', details, name='group-details'),
    path('update/<str:pk>/', update, name='group-update'),
    path('delete/<str:pk>/', delete, name='group-delete'),
]