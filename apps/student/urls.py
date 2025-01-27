from django.urls import path
from .views  import *

urlpatterns = [
    path('details/<str:pk>/', details, name='student-details'),
    path('list/', list, name='student-list'),
    path('create/', create, name='student-create'),
    path('delete/<str:pk>/', delete, name='student-delete'),
    path('rating-list/', rating_list, name='student-rating-list'),
    path('rating-details/<int:pk>/', rating_details, name='student-rating-details'),
]