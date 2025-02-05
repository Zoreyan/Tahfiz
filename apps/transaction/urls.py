from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list, name='transaction-list'),
    path('create/<int:pk>', create, name='transaction-create'),
    path('delete/<int:pk>/<int:student>', delete, name='transaction-delete'),
]