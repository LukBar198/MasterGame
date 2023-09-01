from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class GameMaster(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_game_master = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.nickname


class Player(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_player = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.nickname


class GameSession(models.Model):
    class GameSystem(models.TextChoices):
        RPG1 = 'Rpg1', 'Fajny system'
        RPG2 = 'Rpg2', 'Dobry system'
        RPG3 = 'Rpg3', 'Taki sobie system'
        NONAME = 'NN', 'Inny system'

    owner = models.ForeignKey(GameMaster, on_delete=models.CASCADE)
    system = models.CharField(max_length=4, choices=GameSystem.choices, default=GameSystem.NONAME)
    creation_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    slots = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    session_date = models.DateTimeField()

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.title
