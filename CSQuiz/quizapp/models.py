from django.db import models
# Create your models here.
class Players(models.Model):
    profile_number = models.IntegerField(unique=True)
    nickname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    team = models.CharField(max_length=30, default='No team')
    major_winner = models.BooleanField(default=False)
    major_MVP = models.BooleanField(default=False)
    full_player_name = models.CharField(max_length=90, default='player')
    region = models.CharField(max_length=90, default='Earth')
    weapon = models.CharField(max_length=60, default='Rifler')
    major_played = models.IntegerField(default=0)
    def __str__(self):
        return self.full_player_name