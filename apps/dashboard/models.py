from django.db import models


class Course(models.Model):
    """Курс"""

    title = models.CharField(max_length=140, null=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
