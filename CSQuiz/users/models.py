from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass


class EmailConfirmCodeHelperModel(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    code = models.IntegerField()
    email = models.EmailField()
    deletion_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=7))


