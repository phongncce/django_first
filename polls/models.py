from datetime import datetime

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.create_date.strftime("%Y-%M-%d")}] {self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.question.id}] {self.choice_text}"
