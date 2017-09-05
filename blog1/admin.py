from django.contrib import admin
from blog1.models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','auth','pub_time')
    list_filter = ('pub_time',)

admin.site.register(Article, ArticleAdmin)