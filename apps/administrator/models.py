from django.db import models
from apps.user.models import User

class Administrator(models.Model):
    """Администратор"""

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        null=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, default='996')


    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return self.name