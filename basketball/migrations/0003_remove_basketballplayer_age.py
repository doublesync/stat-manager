# Generated by Django 5.0.2 on 2024-02-17 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0002_basketballplayer_discorduser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketballplayer',
            name='age',
        ),
    ]