# Generated by Django 5.0.2 on 2024-02-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0007_alter_basketballplayer_discorduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketballplayer',
            name='anomaly',
            field=models.CharField(default='None', max_length=32),
        ),
    ]
