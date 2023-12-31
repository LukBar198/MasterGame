# Generated by Django 4.2.4 on 2023-09-01 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GameMaster_app', '0005_remove_gamemaster_user_id_remove_player_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemaster',
            name='is_game_master',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_player',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gamemaster',
            name='nickname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
