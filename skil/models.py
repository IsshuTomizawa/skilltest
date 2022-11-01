from email.policy import default
from django.db import models

# Create your models here.
'''
class Wquestion(models.Model):
    ques = models.TextField()
    answer = models.IntegerField()

    def __str__(self):
        return self.ques
'''

class Equestion(models.Model):
    number = models.IntegerField(default=0)
    ques = models.TextField()
    sele1 = models.TextField()
    sele2 = models.TextField()
    sele3 = models.TextField()
    answer = models.IntegerField()

    def __str__(self):
        return self.ques

class Nquestion(models.Model):
    ques = models.TextField()
    answer = models.IntegerField()

    def __str__(self):
        return self.ques

class Percent(models.Model):
    ques = models.TextField()
    true = models.IntegerField(default = 0)
    false = models.IntegerField(default = 0)

    def __str__(self):
        return self.ques