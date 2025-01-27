from django.urls import path
from .views import *

urlpatterns = [
    path('group-list/', group_list, name='grade-group-list'),
    path('subject-list/<int:pk>/', subject_list, name='grade-subject-list'),
    path('list/<int:group_pk>/<int:subject_pk>/', list, name='grade-list'),
    path('diary/', diary, name='grade-diary'),
    path('delete/<int:group_pk>/<int:subject_pk>/<int:pk>', delete, name='grade-delete'),
]