# Generated by Django 4.2.4 on 2023-09-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameMaster_app', '0011_alter_charactersheet_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playercharacter',
            options={'ordering': ['-creation_date', 'owner_id']},
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='game_session_id',
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='game_session_id',
            field=models.ManyToManyField(to='GameMaster_app.gamesession'),
        ),
    ]
