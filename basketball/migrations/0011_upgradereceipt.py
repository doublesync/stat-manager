# Generated by Django 5.0.2 on 2024-02-24 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0010_remove_voucherreceipt_player_and_more'),
        ('core', '0002_discorduser_my_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpgradeReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.JSONField()),
                ('failed', models.JSONField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discordUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.discorduser')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basketball.basketballplayer')),
            ],
        ),
    ]
