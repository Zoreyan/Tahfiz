from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='salary-list'),
    path('update/<int:pk>/', update, name='salary-update'),
    path('delete/<int:pk>/', delete, name='salary-delete'),
    path('create/', create, name='salary-create'),
]