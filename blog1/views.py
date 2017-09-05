#coding:utf-8

import re

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django import forms
import markdown
import json


# Create your views here.

def showBlogs(request):
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.order_by('-id')

    for article in articles:
        article.pub_time = article.pub_time.strftime("%Y-%m-%d")
        str1=str(markdown.markdown(text=article.content))
        article.content=re.sub(r'<(\S*?)[^>]*>.*?|<.*? />','', str1 )
        print(article.content)

    # return render(request, 'blog1/index.html', {"articles": articles})
    return render(request, 'blog1/mainsite.html', {"articles": articles})

def writeBlogs(request):
    if request.method == 'POST':
        form = BlogFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return render(request,'blog1/write_answer.html',{'write_answer':form})
            return HttpResponse('保存成功！')

        else:
            print(form.errors)
            error = form.errors
            return render(request, 'blog1/write_answer.html', {'write_answer': error})
    else:
        form = BlogFrom()
    return render(request, 'blog1/write.html', {'form': form})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    print(str(article.title))

    article1 = {
        'title': str(article.title),
        'content': markdown.markdown(text=article.content),
        'auth': str(article.auth),
        'id': article.id,
    }
    return render(request, 'blog1/article_page.html', {"article": json.dumps(article1)})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'bolg1/write.html')
    article = models.Article.objects.get(pk=article_id)

    article = {
        'title': str(article.title),
        'content': article.content,
        'auth': str(article.auth),
        'id': article.id,
    }
    print(article)
    return render(request, 'blog1/edit.html', {'article': json.dumps(article)})


def edit_action(request, article_id):
    title = request.POST.get('title')
    content = request.POST.get('text')
    auth = request.POST.get('author')

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.auth = auth
    article.save()

    return HttpResponseRedirect('/blog1/article/' + str(article_id))


def editor(request):
    if request.method == 'POST':
        new_article = models.Article()
        new_article.auth = request.POST.get('author')
        new_article.content = request.POST.get('text')
        new_article.title = request.POST.get('title')
        new_article.save()
        # return HttpResponse("写入成功！")
        return HttpResponseRedirect('/blog1')
    else:
        return render(request, 'blog1/editor.html')


# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
def test(request):
    article = {'title': '<h1>我对</h1>',
               'content': '<h2> 内容</h2>',
               'auth': '<p>作者</p>',
               }

    # return render(request, 'blog1/test.html', {'article': json.dumps(article)})
    return render(request,'blog1/mainsite.html')


def edit_action1(request):
    titile = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    auth = request.POST.get('atuh', 'AUTH')
    models.Article.objects.create(titile=titile, content=content, auth=auth)
    articles = models.Article.objects.all()
    return render(request, 'blog1/index2.html', {'articles': articles})


def editor_page(requesr, article_id):
    pass


def test1(request):
    text = "# 标题一## 标题二### 标题三 "

    html = markdown.markdown(text=text)
    print(html)
    return HttpResponse(html)
    # return  render(request,'blog1/test.html',{'html':html})


class BlogFrom(forms.ModelForm):
    title = forms.CharField(label='标题', required=True)
    content = forms.Textarea()
    auth = forms.CharField(label='作者', required=True)  # widget=forms.Passwoed()

    class Meta:
        model = models.Article
        fields = ('title', 'content', 'auth')


if __name__ == '__main__':
    print(1)
