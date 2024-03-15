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
    full_player_name = models.CharField(max_length=90, blank=True, null=True, default='player')
    region = models.CharField(max_length=90, blank=True, null=True, default='Earth')
    weapon = models.CharField(max_length=60, blank=True, null=True, default='Rifler')
    def __str__(self):
        return self.full_player_name