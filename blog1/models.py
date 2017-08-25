from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(null=False)
    auth = models.CharField(max_length=5)
    def __str__(self):
        return  self.title