# Generated by Django 3.2.12 on 2022-10-21 07:20

import bson.objectid
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('passwd', models.CharField(max_length=150)),
                ('country', models.CharField(default='FRANCE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ContentText', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(default=4)),
                ('isUsed', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default=bson.objectid.ObjectId, max_length=20)),
                ('startDate', models.DateField(default=datetime.date(2022, 10, 21))),
                ('endDate', models.DateField(default=datetime.date(2022, 10, 28))),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('acces', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('telephone', models.CharField(max_length=25)),
                ('passwd', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avis.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shot', models.ImageField(upload_to='')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avis.account')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avis.content')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avis.session')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avis.user')),
            ],
        ),
    ]
