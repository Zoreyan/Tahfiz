from django.db import models
from apps.user.models import User
from apps.group.models import Group
from apps.student.models import Student
from apps.schedule.models import Subject


class Teacher(models.Model):
    """Преподаватель"""
    image = models.ImageField(upload_to='teacher/', null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True)
    name = models.CharField(max_length=150)
    subjects = models.ManyToManyField(Subject)
    phone = models.CharField(max_length=12, default='996')
    group = models.ManyToManyField(Group)


    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.name





class TeacherReport(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_quantity = models.IntegerField()
    total_student_quantity = models.IntegerField(null=True)
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.SET_NULL, 
        null=True)
    comment = models.TextField()

    def __str__(self):
        return self.teacher.name

    class Meta:
        verbose_name = 'Отчет учителя'
        verbose_name_plural = 'Отчеты учителей'
    


class Code(models.Model):
    value = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.teacher.name

    class Meta:
        verbose_name = 'Посещаемость'
        verbose_name_plural = 'Посещаемость'