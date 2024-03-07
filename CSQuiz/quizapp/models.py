from django.db import models

# Create your models here.
class Players(models.Model):
    profile_number = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    team = models.CharField(max_length=30)
    major_winner = models.BooleanField()
    major_mvp = models.BooleanField()


    def __str__(self):
        return f"{name} '{nickname}' {surname}"