# Generated by Django 5.0.2 on 2024-02-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0015_auto_generated_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketballteam',
            name='city',
        ),
        migrations.RemoveField(
            model_name='basketballteam',
            name='titles',
        ),
        migrations.AddField(
            model_name='basketballteam',
            name='color',
            field=models.CharField(default='#434648', max_length=32),
        ),
    ]
