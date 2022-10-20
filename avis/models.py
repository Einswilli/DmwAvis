from email.policy import default
from django.db import models

# Create your models here.

########
####        TEXTS
########
class Content(models.Model):
    id=models.AutoField(primary_key=True)
    ContentText=models.TextField(blank=True,null=True)
    isUsed=models.BooleanField(default=False)
    createdAt=models.DateTimeField(auto_now_add=True)


########
####        COMPTES VIRTUELS
########
class Poster(models.Model):
    id=models.AutoField(primary_key=True)
    fullName=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    passwd=models.CharField(max_length=150)
    country=models.CharField(max_length=100,default='FRANCE')


########
####        COMPTES VIRTUELS
########
