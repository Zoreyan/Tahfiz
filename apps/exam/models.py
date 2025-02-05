from django.db import models
from apps.user.models import User
from apps.group.models import Group


class Exam(models.Model):
    title = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_points = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'


class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class StudentExam(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, default=0)
    answers = models.ManyToManyField(Answer)
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)