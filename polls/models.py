from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('Published Date', null=True)

    def __str__(self):
        return f"[{self.create_date.strftime("%Y-%m-%d")}] {self.question_text}"

    def was_recent(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.create_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.question.id}] {self.choice_text}"
