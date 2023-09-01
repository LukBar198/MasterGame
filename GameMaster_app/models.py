from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class GameMaster(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_nickname = models.CharField(max_length=128, default='')
    is_game_master = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date', 'nickname']

    def __str__(self):
        return self.user_nickname


class Player(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    player_nickname = models.CharField(max_length=128, default='')
    is_player = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date', 'user_id']

    def __str__(self):
        return self.player_nickname


class GameSession(models.Model):
    class GameSystem(models.TextChoices):
        RPG1 = 'Rpg1', 'Fajny system'
        RPG2 = 'Rpg2', 'Dobry system'
        RPG3 = 'Rpg3', 'Taki sobie system'
        NONAME = 'NN', 'Inny system'

    owner_id = models.ForeignKey(GameMaster, on_delete=models.CASCADE)
    system = models.CharField(max_length=4, choices=GameSystem.choices, default=GameSystem.NONAME)
    creation_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    slots = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    session_date = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)

    class Meta:
        ordering = ['-creation_date', 'owner_id', 'session_date']

    def __str__(self):
        return self.title


class PlayerCharacter(models.Model):
    class CharacterStatus(models.TextChoices):
        DEAD = 'Dead', 'Martwy'
        ALIVE = 'Alive', 'Żyje'

    owner_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    character_status = models.CharField(max_length=5, choices=CharacterStatus.choices, default=CharacterStatus.ALIVE)
    game_session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-creation_date', 'owner_id', 'game_session_id']

    def __str__(self):
        return self.name


class CharacterSheet(models.Model):
    character_id = models.OneToOneField(PlayerCharacter, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=128)
    creation_date = models.DateTimeField(default=timezone.now)
    strength = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    condition = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    dexterity = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    intelligence = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    wisdom = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    charisma = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(30)])
    reputation = models.IntegerField(default=0)
    wealth = models.PositiveIntegerField(default=0)
    life_points = models.PositiveIntegerField(default=10, validators=[MaxValueValidator(100)])
    age = models.PositiveIntegerField(default=20, validators=[MinValueValidator(18), MaxValueValidator(999)])

    class Meta:
        ordering = ['-creation_date', 'character_id']

    def __str__(self):
        return self.name
