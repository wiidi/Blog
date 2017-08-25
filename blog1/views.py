from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django import forms
# Create your views here.

class BlogFrom(forms.ModelForm):
    title = forms.CharField(label='标题',required=True)
    content = forms.Textarea()
    auth = forms.CharField(label='作者' ,required=True) # widget=forms.Passwoed()
    class Meta:
        model = models.Article
        fields=('title','content','auth')

def showBlogs(request):

    # article = models.Article.objects.get(pk=1)
    article = models.Article.objects.all()
    # article='wudi'
    return render(request,'blog1/index.html',{"article":article})
    # return HttpResponse("blog")

def writeBlogs(request):
    if request.method == 'POST':
        form = BlogFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'blog1/write_answer.html',{'write_answer':form})
        else:
            print(form.errors)
            error = form.errors
            return render(request, 'blog1/write_answer.html', {'write_answer':error})
    else:
        form = BlogFrom()
    return render(request,'blog1/write.html',{'form':form})
