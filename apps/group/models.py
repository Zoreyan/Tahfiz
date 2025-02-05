from django.db import models
from apps.dashboard.models import Course


class Group(models.Model):
    """Группа"""

    title = models.CharField(max_length=40, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title