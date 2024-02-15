# Generated by Django 5.0.2 on 2024-02-14 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasketballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('wingspan', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('age', models.CharField(max_length=32)),
                ('archetype', models.CharField(choices=[('Skilled', 'Skilled'), ('Athletic', 'Athletic'), ('Giant', 'Giant')], max_length=10)),
                ('position', models.CharField(choices=[('PG', 'PG'), ('SG', 'SG'), ('SF', 'SF'), ('PF', 'PF'), ('C', 'C')], max_length=2)),
                ('secondary_position', models.CharField(choices=[('PG', 'PG'), ('SG', 'SG'), ('SF', 'SF'), ('PF', 'PF'), ('C', 'C')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='BasketballTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('titles', models.IntegerField()),
                ('players', models.ManyToManyField(to='basketball.basketballplayer')),
            ],
        ),
        migrations.AddField(
            model_name='basketballplayer',
            name='current_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basketball.basketballteam'),
        ),
    ]
