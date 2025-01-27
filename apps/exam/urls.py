from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='exam-list'),
    path('create/', create, name='exam-create'),
    path('update/<int:pk>/', update, name='exam-update'),
    path('delete/<int:pk>/', delete, name='exam-delete'),
    path('details/<int:pk>/', details, name='exam-details'),

    path('start/<int:pk>/<int:question_id>/', start, name='exam-start'),
    path('finish/<int:pk>/', finish, name='exam-finish'),
    path('result-list/', result_list, name='exam-result-list'),
    path('result-details/<int:pk>/', result_details, name='exam-result-details'),
    path('student-exam-list/', student_exam_list, name='student-exam-list'),
    
    path('question-create/<int:pk>/', question_create, name='exam-question-create'),
    path('question-delete/<int:pk>/', question_delete, name='exam-question-delete'),
    path('answer-create/<int:pk>/', answer_create, name='exam-answer-create'),
    path('answer-delete/<int:pk>/', answer_delete, name='exam-answer-delete'),
]