from django.urls import path
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('student/', StudentRetrieveView.as_view(), name='student_retrieve_api'),
    path('students/', StudentListView.as_view(), name='students_retrieve_api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('schedule/', ScheduleAPIView.as_view(), name='schedule_api'),
    path('schedules/all/', AllSchedulesAPIView.as_view(), name='all_schedules_api'),
    path('group/<int:pk>/', GroupRetrieveView.as_view(), name='group_retrieve_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('diary/', DiaryAPIView.as_view(), name='diary_api'),
    path('transaction/', TransactionListAPIView.as_view(), name='transaction_list_api'),
]