from django.db import models
from apps.student.models import Student
from apps.teacher.models import Teacher
from apps.schedule.models import Subject



class Grade(models.Model):
    """Оценка студента"""

    student = models.ForeignKey(
        Student,
        verbose_name="Студент",
        on_delete=models.SET_NULL,
        null=True)

    mark = models.FloatField(verbose_name="Оценка")
    pages = models.FloatField(verbose_name="Страницы", null=True)
    subject = models.ForeignKey(
        Subject,
        verbose_name="Предмет",
        on_delete=models.SET_NULL,
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        verbose_name="Преподаватель",
        on_delete=models.SET_NULL,
        null=True)

    date = models.DateField(verbose_name="День", auto_now_add=False)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
    
    def __str__(self):
        return '-'