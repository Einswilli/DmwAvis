# Generated by Django 3.2.12 on 2022-10-22 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avis', '0004_alter_session_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isRejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='isValidated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='code',
            field=models.CharField(default='6353cac2c19369f6d172dff1', max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='endDate',
            field=models.DateField(default=datetime.date(2022, 10, 29)),
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateField(default=datetime.date(2022, 10, 22)),
        ),
    ]
