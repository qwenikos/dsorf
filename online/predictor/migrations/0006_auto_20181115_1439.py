# Generated by Django 2.1.2 on 2018-11-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0005_auto_20181115_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputmodel',
            name='simulateLength',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
