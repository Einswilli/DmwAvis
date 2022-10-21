import datetime
from bson.objectid import ObjectId
from django.db import models
from django.utils.timezone import now as dj_now
from dateutil.relativedelta import relativedelta

# Create your models here.

########
####        TEXTS
########
class Content(models.Model):
    id=models.AutoField(primary_key=True)
    ContentText=models.TextField(blank=True,null=True)
    stars=models.IntegerField(default=4)
    isUsed=models.BooleanField(default=False)
    createdAt=models.DateTimeField(auto_now_add=True)


########
####        COMPTES VIRTUELS
########
class Account(models.Model):
    id=models.AutoField(primary_key=True)
    fullName=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    passwd=models.CharField(max_length=150)
    country=models.CharField(max_length=100,default='FRANCE')


########
####        TYPES D'UTILISATEURS
########
class UserType(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    acces=models.CharField(max_length=80)


########
####        COMPTES DES UTILISATEURS
########
class User(models.Model):
    id=models.AutoField(primary_key=True)
    lname=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    telephone=models.CharField(max_length=25)
    passwd=models.CharField(max_length=50)
    type=models.ForeignKey("UserType",on_delete=models.CASCADE)


########
####        AVIS POSTÉS
########
class Session(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.CharField(max_length=20,default=ObjectId)
    startDate=models.DateField(default=datetime.date.today())
    endDate=models.DateField(default=datetime.date.today()+relativedelta(days=int(7)))


########
####        AVIS POSTÉS
########
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey("User",on_delete=models.CASCADE,null=True,blank=True)
    content=models.ForeignKey("Content",on_delete=models.CASCADE)
    account=models.ForeignKey("Account",on_delete=models.CASCADE)
    session=models.ForeignKey("Session",on_delete=models.CASCADE)
    shot=models.ImageField()
