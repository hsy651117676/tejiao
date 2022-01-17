from django.db import models

class menu(models.Model):
    id= models.AutoField(primary_key=True)
    pid= models.CharField(max_length=12)
    mid= models.CharField(max_length=12)
    level= models.IntegerField(null=True)
    melement= models.CharField(max_length=1024,null=True,unique=False)
    mtitle= models.CharField(max_length=1024,null=True,unique=False)
    mclass= models.CharField(max_length=1024,null=True,unique=False)
    mdataoption= models.CharField(max_length=1024,null=True,unique=False)
    mstyle= models.CharField(max_length=1024,null=True,unique=False)
    msrc= models.CharField(max_length=1024,null=True,unique=False)
    mhref= models.CharField(max_length=1024,null=True,unique=False)

