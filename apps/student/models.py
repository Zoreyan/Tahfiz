from django.db import models
from apps.user.models import User
from apps.group.models import Group
from django.db.models import Q, Avg
from apps.schedule.models import *
from datetime import datetime

class Student(models.Model):
    """Студент"""
    image = models.ImageField(upload_to='student/', null=True)
    to_pay = models.IntegerField(null=True)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        null=True)
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    phone = models.CharField(max_length=12, default='996')
    group = models.ManyToManyField(Group)


    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


    def __str__(self):
        return self.name
    

    @property
    def total_amount(self):
        transactions = self.transaction_set.all()
        total = sum([item.amount for item in transactions])
        return total


    @property
    def show_grade(self):
        data_list = [''] * 31
        marks = self.mark_set.filter(day__month = datetime.now().month)
        for i in marks:
            data_list[i.day.day-1] = i.mark
        return data_list
    

    def semester_access(self):
        return True

    @property
    def payed(self):
        return sum(i.amount for i in self.transaction_set.filter(Q(date__month=datetime.now().month) & Q(date__year=datetime.now().year)))
    
