from django.db import models
from apps.teacher.models import Teacher


class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    updated = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.teacher.name

    @property
    def get_remainder(self):
        return self.total_amount - self.amount


    class Meta:
        verbose_name = 'Зарплата учителя'
        verbose_name_plural = 'Зарплаты учителей'