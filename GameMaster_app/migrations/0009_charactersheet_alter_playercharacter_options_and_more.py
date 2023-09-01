# Generated by Django 4.2.4 on 2023-09-01 19:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GameMaster_app', '0008_gamesession_is_open_gamesession_is_public_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterSheet',
            fields=[
                ('character_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='GameMaster_app.playercharacter')),
                ('name', models.CharField(max_length=128)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('strength', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('condition', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('dexterity', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('intelligence', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('wisdom', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('charisma', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('reputation', models.IntegerField(default=0)),
                ('wealth', models.PositiveIntegerField(default=0)),
                ('life_points', models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100)])),
                ('age', models.PositiveIntegerField(default=20, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='playercharacter',
            options={'ordering': ['-creation_date']},
        ),
        migrations.RenameField(
            model_name='gamesession',
            old_name='owner',
            new_name='owner_id',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='nickname',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='playercharacter',
            old_name='game_session',
            new_name='game_session_id',
        ),
        migrations.RenameField(
            model_name='playercharacter',
            old_name='owner',
            new_name='owner_id',
        ),
        migrations.AddField(
            model_name='gamemaster',
            name='user_nickname',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='player',
            name='player_nickname',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='playercharacter',
            name='character_status',
            field=models.CharField(choices=[('Dead', 'Martwy'), ('Alive', 'Żyje')], default='Alive', max_length=5),
        ),
    ]
