# Generated by Django 2.1.2 on 2018-11-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='inputTypeFormItem',
            field=models.BooleanField(choices=[(True, 'Sequence'), (False, 'File')], default=False),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='fileNameFormItem',
            field=models.FileField(upload_to='./%d/%m/%Y/'),
        ),
    ]