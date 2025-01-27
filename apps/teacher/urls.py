from django.urls import path
from .views  import *

urlpatterns = [
    path('list/', list, name='teacher-list'),
    path('create/', create, name='teacher-create'),
    path('details/<str:pk>/', details, name='teacher-details'),
    
    path('students/', students, name='teacher-students'),
    path('report-list/', report_list, name='teacher-report-list'),
    path('delete/<str:pk>/', delete, name='teacher-delete'),

    path('generated-code/', generated_code, name='teacher-generated-code'),
    path('code/', code, name='teacher-code'),

    path('attendance/', attendance_list, name='attendance-list'),
]