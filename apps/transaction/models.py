from django.db import models
from apps.student.models import Student


class Transaction(models.Model):

    TYPES = (
        ('education', 'Оплата за обучение'),
        ('food', 'Оплата за питание'),
    )

    SEMESTERS = (
        ('1', '1'),
        ('2', '2'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    semester = models.CharField(max_length=1, choices=SEMESTERS, default='1')
    type = models.CharField(max_length=10, choices=TYPES, default='education')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
    
    def __str__(self):
        return f'{self.student.name}'