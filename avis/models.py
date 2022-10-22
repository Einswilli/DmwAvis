import datetime
from email.policy import default
from bson.objectid import ObjectId
from django.db import models
from django.utils.timezone import now as dj_now
from dateutil.relativedelta import relativedelta

# Create your models here.

########
####        AVIS POSTÉS
########
class Session(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.CharField(max_length=50,default=str(ObjectId()))
    isActive=models.BooleanField(default=True)
    startDate=models.DateField(default=datetime.date.today())
    endDate=models.DateField(default=datetime.date.today()+relativedelta(days=int(7)))

    def down(self):
        self.isActive=False
        self.save()


########
####        TEXTS
########
class Content(models.Model):
    id=models.AutoField(primary_key=True)
    ContentText=models.TextField(blank=True,null=True)
    stars=models.IntegerField(default=4)
    gender=models.TextChoices('F','M')
    isUsed=models.BooleanField(default=False)
    user=models.ForeignKey("User",on_delete=models.CASCADE,null=True,blank=True)
    session=models.ForeignKey("Session",on_delete=models.CASCADE,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    def assignTo(self,id):
        self.user=User.objects.get(id=id)
        self.isUsed=True
        self.save()

    def truncate(self):
        return self.ContentText[0:80]+'...' if len(self.ContentText)>80 else self.ContentText


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
####        COMPTES VIRTUELS
########
class Account(models.Model):
    id=models.AutoField(primary_key=True)
    fullName=models.CharField(max_length=100)
    email=models.CharField(max_length=150,null=True)
    passwd=models.CharField(max_length=150)
    isOccupy=models.BooleanField(default=False)
    assignedTo=models.ForeignKey("User",on_delete=models.CASCADE,null=True,blank=True)
    country=models.CharField(max_length=100,default='FRANCE')

    def assign_user(self,id):
        self.assignedTo=User.objects.get(id=id)
        self.isOccupy=True
        self.save()

    def supply_email(self,email):
        self.email=email
        self.save()


########
####        AVIS POSTÉS
########
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey("User",on_delete=models.CASCADE,null=True,blank=True)
    content=models.ForeignKey("Content",on_delete=models.CASCADE)
    account=models.ForeignKey("Account",on_delete=models.CASCADE)
    session=models.ForeignKey("Session",on_delete=models.CASCADE)
    isValidated=models.BooleanField(default=False)
    isRejected=models.BooleanField(default=False)
    shot=models.ImageField(null=True,blank=True)

    def validate(self):
        self.isValidated=True
        self.isRejected=False
        self.save()

    def reject(self):
        self.isValidated=False
        self.isRejected=True
        self.save()
