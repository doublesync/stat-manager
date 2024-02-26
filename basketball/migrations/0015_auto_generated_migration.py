from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0014_alter_basketballplayer_jumpshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashreceipt',
            name='payReason',
            field=models.CharField(max_length=30, default='None'),
        ),
        migrations.AddField(
            model_name='cashreceipt',
            name='jobType',
            field=models.CharField(max_length=10, default='Misc'),
        ),
    ]
