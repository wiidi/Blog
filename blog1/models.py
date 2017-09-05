from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(null=False)
    auth = models.CharField(max_length=5)
    pub_time = models.DateTimeField(auto_now=False,default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return  self.title

