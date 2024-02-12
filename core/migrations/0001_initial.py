# Generated by Django 5.0.2 on 2024-02-11 23:52

import core.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('discord_tag', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('public_flags', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('locale', models.CharField(max_length=100)),
                ('mfa_enabled', models.BooleanField()),
                ('last_login', models.DateTimeField(null=True)),
                ('last_reward', models.DateTimeField(null=True)),
            ],
            managers=[
                ('objects', core.managers.DiscordAuthorizationManager()),
            ],
        ),
    ]