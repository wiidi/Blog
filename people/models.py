from django.db import models

# Create your models here.

# Create your models here.
class People(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length= 30)