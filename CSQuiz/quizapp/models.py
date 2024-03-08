from django.db import models

# Create your models here.
class Players(models.Model):
    profile_number = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    team = models.CharField(max_length=30, blank=True, null=True)
    major_winner = models.BooleanField(blank=True, null=True)
    major_MVP = models.BooleanField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} '{self.nickname}' {self.surname}"