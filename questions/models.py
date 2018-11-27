from django.db import models
from ordered_model.models import OrderedModel
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Choice(OrderedModel):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)
