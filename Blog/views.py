from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader

def showBlog(request):
    blog_content= "this is blog content!"
    auth = "wudi"
    title = 'this is title'
    content={}
    content['blog'] = blog_content
    content['auth'] = auth
    content["title"] = title

    # Blog = Blog.objects.get(id=blog_id)

    return render(request,'index.html',content)

def showBlogList(request):

    pass
