# Generated by Django 4.2.4 on 2023-09-01 17:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GameMaster_app', '0007_alter_gamemaster_options_alter_player_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesession',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('character_status', models.CharField(choices=[('Dead', 'Żyje'), ('Alive', 'Martwy')], default='Alive', max_length=5)),
                ('game_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMaster_app.gamesession')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameMaster_app.player')),
            ],
        ),
    ]