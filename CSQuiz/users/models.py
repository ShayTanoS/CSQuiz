from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    quizzes_win = models.IntegerField(default=0)
    quizzes_lose = models.IntegerField(default=0)

