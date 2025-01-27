from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Пользователь"""

    ROLES = (
        ('admin', 'Админ'),
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('administrator', 'Администратор'),
    )
    role = models.CharField(
        null=True,
        choices=ROLES,
        max_length=20,
        )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []