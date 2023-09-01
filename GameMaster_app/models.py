from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class GameMaster(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_game_master = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)


class Player(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_player = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)
