# Generated by Django 4.2.4 on 2023-08-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameMaster_app', '0002_rename_user_gamemaster_user_id_gamemaster_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemaster',
            name='nickname',
            field=models.CharField(max_length=64),
        ),
    ]
