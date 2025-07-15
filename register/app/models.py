from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    city=models.CharField(max_length=50)
    contact=models.IntegerField()
    document=models.FileField(upload_to='file/')
