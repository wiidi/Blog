from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(null=False)
    auth = models.CharField(max_length=5)