# Generated by Django 3.2.12 on 2022-10-22 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avis', '0005_auto_20221022_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avis.session'),
        ),
        migrations.AlterField(
            model_name='session',
            name='code',
            field=models.CharField(default='6353f053341248a6dd7e07c1', max_length=50),
        ),
    ]
