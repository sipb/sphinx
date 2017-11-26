from django.db import models

class Poll(models.Model):
    question_1 = models.CharField(max_length=30)
    question_2 = models.CharField(max_length=30)
