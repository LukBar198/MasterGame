from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class GameMaster(models.Model):
    """
    GameMaster is a Django model representing a user with game master privileges.

    This model extends the built-in User model and adds additional fields to represent
    game master-specific information.

    Fields:
    - user_id (OneToOneField): A one-to-one relationship with the User model, serving as the
      primary key for this model.
    - user_nickname (CharField): A character field to store the nickname or display name
      of the game master.
    - is_game_master (BooleanField): A boolean field indicating whether the user has game
      master privileges.
    - creation_date (DateTimeField): A datetime field recording the date and time when
      the GameMaster instance was created.

    Meta:
    - ordering (list): Specifies the default ordering for instances of this model. The list
      contains two elements: '-creation_date' for descending order by creation date and
      'user_id' for ascending order by user ID.

    Methods:
    - __str__(): Returns the user's nickname as the string representation of this model.
    """
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_nickname = models.CharField(max_length=128, default='')
    is_game_master = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date', 'user_id']

    def __str__(self):
        return self.user_nickname


class Player(models.Model):
    """
    Player is a Django model representing a regular user or player in a gaming application.

    This model extends the built-in User model and adds additional fields to represent
    player-specific information.

    Fields:
    - user_id (OneToOneField): A one-to-one relationship with the User model, serving as the
      primary key for this model.
    - player_nickname (CharField): A character field to store the nickname or display name
      of the player.
    - is_player (BooleanField): A boolean field indicating whether the user is a regular player.
    - creation_date (DateTimeField): A datetime field recording the date and time when
      the Player instance was created.

    Meta:
    - ordering (list): Specifies the default ordering for instances of this model. The list
      contains two elements: '-creation_date' for descending order by creation date and
      'user_id' for ascending order by user ID.

    Methods:
    - __str__(): Returns the player's nickname as the string representation of this model.
    """
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    player_nickname = models.CharField(max_length=128, default='')
    is_player = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date', 'user_id']

    def __str__(self):
        return self.player_nickname


class GameSession(models.Model):
    """
    GameSession is a Django model representing a gaming session.

    This model stores information about gaming sessions, including session title, owner,
    available slots, session date, and accessibility settings.

    Fields:
    - owner_id (ForeignKey): A many-to-one relationship with the GameMaster model, representing
      the owner / game master of the session.
    - creation_date (DateTimeField): A datetime field recording the date and time when
      the GameSession instance was created.
    - title (CharField): A character field to store the title or name of the gaming session.
    - slots (PositiveIntegerField): An integer field representing the number of available slots
      for players, with validation to ensure a minimum of 1 and a maximum of 6 slots.
    - session_date (DateTimeField): A datetime field representing the date and time of the gaming session.
    - is_public (BooleanField): A boolean field indicating whether the session is public or private.
    - is_open (BooleanField): A boolean field indicating whether the session is open or closed to players.

    Meta:
    - ordering (list): Specifies the default ordering for instances of this model. The list
      contains three elements: '-creation_date' for descending order by creation date,
      'owner_id' for ascending order by owner ID, and 'session_date' for ascending order by session date.

    Methods:
    - __str__(): Returns the title of the gaming session as the string representation of this model.
    """
    owner_id = models.ForeignKey(GameMaster, on_delete=models.CASCADE)
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


class GameSystem(models.Model):
    """
        GameSystem is a Django model representing the gaming system used in a gaming session.

        This model allows users to specify the gaming system being used for a particular gaming session.

        Fields:
        - session_id (ForeignKey): A many-to-one relationship with the GameSession model, indicating
          the gaming session associated with this gaming system choice.
        - system (CharField with choices): A character field representing the gaming system choice,
          with predefined choices provided by the GameSystemChoices class.
        - creation_date (DateTimeField): A datetime field recording the date and time when
          the GameSystem instance was created.

        Meta:
        - ordering (list): Specifies the default ordering for instances of this model. The list
          contains two elements: '-creation_date' for descending order by creation date and
          'session_id' for ascending order by associated session ID.

        Methods:
        - __str__(): Returns the name of the gaming system as the string representation of this model.
        """
    class GameSystem(models.TextChoices):
        RPG1 = 'Rpg1', 'Fajny system'
        RPG2 = 'Rpg2', 'Dobry system'
        RPG3 = 'Rpg3', 'Taki sobie system'
        NONAME = 'NN', 'Inny system'

    session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    system = models.CharField(max_length=4, choices=GameSystem.choices, default=GameSystem.NONAME)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creation_date', 'session_id']

    def __str__(self):
        return self.system


class PlayerCharacter(models.Model):
    """
        PlayerCharacter is a Django model representing a player's character in a gaming session.

        This model allows users to create and manage player characters for gaming sessions.

        Fields:
        - owner_id (ForeignKey): A many-to-one relationship with the Player model, indicating the
          owner / player associated with this character.
        - name (CharField): A character field to store the name or title of the character.
        - description (TextField): A text field for providing a description or background story
          for the character.
        - creation_date (DateTimeField): A datetime field recording the date and time when
          the PlayerCharacter instance was created.
        - character_status (CharField with choices): A character field representing the status
          of the character, with predefined choices provided by the CharacterStatusChoices class.
        - game_session_id (ManyToManyField): A many-to-many relationship with the GameSession model,
          allowing the character to be associated with multiple gaming sessions.

        Meta:
        - ordering (list): Specifies the default ordering for instances of this model. The list
          contains two elements: '-creation_date' for descending order by creation date and
          'owner_id' for ascending order by owner ID.

        Methods:
        - __str__(): Returns the name of the character as the string representation of this model.
        """
    class CharacterStatus(models.TextChoices):
        DEAD = 'Dead', 'Martwy'
        ALIVE = 'Alive', 'Żyje'

    owner_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    character_status = models.CharField(max_length=5, choices=CharacterStatus.choices, default=CharacterStatus.ALIVE)
    game_session_id = models.ManyToManyField('GameSession')

    class Meta:
        ordering = ['-creation_date', 'owner_id']

    def __str__(self):
        return self.name


class CharacterSheet(models.Model):
    """
    CharacterSheet is a Django model representing the attributes and statistics of a player character.

    This model allows users to store and manage various attributes and statistics for a player character
    in a gaming session.

    Fields:
    - character_id (OneToOneField): A one-to-one relationship with the PlayerCharacter model, indicating
      the player character associated with this character sheet.
    - strength (PositiveIntegerField): An integer field to represent the strength attribute of the character,
      with default values and validators.
    - condition (PositiveIntegerField): An integer field to represent the condition attribute of the character,
      with default values and validators.
    - dexterity (PositiveIntegerField): An integer field to represent the dexterity attribute of the character,
      with default values and validators.
    - intelligence (PositiveIntegerField): An integer field to represent the intelligence attribute of the character,
      with default values and validators.
    - wisdom (PositiveIntegerField): An integer field to represent the wisdom attribute of the character,
      with default values and validators.
    - charisma (PositiveIntegerField): An integer field to represent the charisma attribute of the character,
      with default values and validators.
    - reputation (IntegerField): An integer field to represent the reputation of the character, with a default
      value.
    - wealth (PositiveIntegerField): An integer field to represent the wealth of the character, with a default
      value.
    - life_points (PositiveIntegerField): An integer field to represent the life points of the character,
      with a default value and maximum value validator.
    - age (PositiveIntegerField): An integer field to represent the age of the character, with default values
      and validators.

    Meta:
    - ordering (list): Specifies the default ordering for instances of this model. The list contains one element:
      '-character_id' for descending order by associated character ID.

    Methods:
    - __str__(): Returns the string representation of the associated player character.
    """
    character_id = models.OneToOneField(PlayerCharacter, on_delete=models.CASCADE, primary_key=True)
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
        ordering = ['-character_id']

    def __str__(self):
        return self.character_id
