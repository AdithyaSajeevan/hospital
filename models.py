from django.db import models


# Create your models here.
class Doctor(models.Model):
    Dr_name = models.CharField(max_length = 200)
    specialisation = models.CharField(max_length = 200)
    image=models.ImageField(upload_to='media',default="")
    mobile = models.IntegerField(null = True) 
    
class Patient(models.Model):

    name = models.CharField(max_length = 200)
    age = models.IntegerField(null = True)
    mobile = models.IntegerField(null = True)
    gender = models.CharField(max_length=10, null=True)
    disease = models.CharField(max_length=50, null=True)
    doctor = models.CharField(max_length=50, null=True) 