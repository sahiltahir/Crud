from django.db import models

# Create your models here.
class StudentData(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phoneno=models.BigIntegerField()
    marks1=models.IntegerField()
    marks2=models.IntegerField()
    marks3=models.IntegerField()
    marks4=models.IntegerField()