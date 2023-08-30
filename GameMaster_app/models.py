from django.db import models
from django.utils import timezone


class User(models.Model):
    nickname = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    is_game_master = models.BooleanField(default=False)
    is_player = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
