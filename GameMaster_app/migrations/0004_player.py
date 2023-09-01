# Generated by Django 4.2.4 on 2023-08-30 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GameMaster_app', '0003_alter_gamemaster_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_id', models.OneToOneField(limit_choices_to={'is_player': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='GameMaster_app.user')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('nickname', models.CharField(max_length=64)),
            ],
        ),
    ]