# Generated by Django 2.1.2 on 2018-11-15 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0006_auto_20181115_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputmodel',
            old_name='modelFormItem',
            new_name='modeFormItem',
        ),
    ]