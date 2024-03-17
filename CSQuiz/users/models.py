from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    quizzes_win = models.IntegerField(default=0)
    quizzes_lose = models.IntegerField(default=0)


class EmailConfirmCodeHelperModel(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    code = models.IntegerField()
    email = models.EmailField()
    deletion_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=123))


