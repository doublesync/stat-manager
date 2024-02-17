# Generated by Django 5.0.2 on 2024-02-17 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0003_remove_basketballplayer_age'),
        ('core', '0002_discorduser_my_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketballplayer',
            name='currentTeam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basketball.basketballteam'),
        ),
        migrations.AlterField(
            model_name='basketballplayer',
            name='discordUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.discorduser'),
        ),
    ]
