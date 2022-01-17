from django.db import models
# Create your models here.

class sch_type(models.Model):
    rowid= models.IntegerField(null=True)
    schooltype= models.CharField(max_length=30,null=True,unique=False)
    code= models.CharField(max_length=30,null=True,unique=False)

class stu_info(models.Model):
    stuid= models.IntegerField(null=True)
    name= models.CharField(max_length=30,null=True,unique=False)
    sex= models.CharField(max_length=30,null=True,unique=False)
    birth= models.CharField(max_length=30,null=True,unique=False)
    age= models.CharField(max_length=30,null=True,unique=False)
    nation= models.CharField(max_length=30,null=True,unique=False)
    photo= models.CharField(max_length=30,null=True,unique=False)
    address=models.CharField(max_length=30,null=True,unique=False)
    register=models.CharField(max_length=30,null=True,unique=False)
    tel=models.CharField(max_length=30,null=True,unique=False)
    idcard=models.CharField(max_length=18,null=True,unique=False)
    disabilityid=models.CharField(max_length=30,null=True,unique=False)
    classification=models.CharField(max_length=30,null=True,unique=False)
    grade=models.CharField(max_length=30,null=True,unique=False)
    disease=models.CharField(max_length=30,null=True,unique=False)
    paerntal=models.CharField(max_length=30,null=True,unique=False)
    family=models.CharField(max_length=30,null=True,unique=False)
    remarks=models.CharField(max_length=30,null=True,unique=False)

class stu_enrol(models.Model):
    stuid= models.IntegerField(null=True,unique=True)
    attendSchool=models.CharField(max_length=30,null=True,unique=False)
    grade=models.CharField(max_length=30,null=True,unique=False)
    situation=models.CharField(max_length=30,null=True,unique=False)
    
class stu_family(models.Model):
    stuid= models.IntegerField(null=True,unique=True)
    name=models.CharField(max_length=30,null=True,unique=False)
    appellation=models.CharField(max_length=30,null=True,unique=False)
    idcard=models.CharField(max_length=18,null=True,unique=False)
    job=models.CharField(max_length=30,null=True,unique=False)
    duties=models.CharField(max_length=30,null=True,unique=False)
    tel=models.CharField(max_length=30,null=True,unique=False)
 
class stu_viability(models.Model):
    stuid= models.IntegerField(null=True,unique=True)
    skillid= models.IntegerField(null=True,unique=True)
    score= models.IntegerField(null=True,unique=True)

class zb_viability(models.Model):
    skillid= models.IntegerField(null=True,unique=True)
    num= models.IntegerField(null=True,unique=False)
    text=models.CharField(max_length=80,null=True,unique=False)
    level= models.IntegerField(null=True,unique=False)

class zb_strengthen(models.Model):
    sid= models.IntegerField(null=True,unique=True)
    text=models.CharField(max_length=80,null=True,unique=False)
    num= models.IntegerField(null=True,unique=False)
    text=models.CharField(max_length=80,null=True,unique=False)
    level= models.IntegerField(null=True,unique=False)
