from django.db import models

# Create your models here.

class Api(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    City = models.CharField(max_length=50)
    Contact = models.CharField(max_length=15)
    
