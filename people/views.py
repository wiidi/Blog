from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from people.models import People
from django import forms
import django.contrib.staticfiles


def index(request):
    return render(request, 'index2.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        try:
            user = People.objects.get(username=username, passwd=passwd)
        except:
            return HttpResponse('用户名或密码错误！%s : %s' % (username, passwd))
        if user:
            return HttpResponseRedirect('/blog1/')
    else:
        return render(request, 'people/login_register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        return HttpResponse("注册成功！")

    return render(request, 'people/login_register.html')


def test(request):
    return render(request, 'people/login_register.html')

# class PeopleForm(forms.ModelForm):
#     username = forms.CharField(label='账号', required=True)
#     passwd = forms.CharField(label='密码', required=True, widget=forms.PasswordInput)
#
#     class Meta:
#         model = People
#         fields = ('username', 'passwd')


# def login(request):
#     if request.method == 'POST':
#         form = PeopleForm(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data['username']
#             # passwd = form.changed_data['passwd']
#             username = request.POST.get('username')
#             passwd = request.POST.get('passwd')
#
#             # username = form['username']
#             # passwd = form['passwd']
#             try:
#                 user = People.objects.get(username=username, passwd=passwd)
#             except:
#                 return HttpResponse('用户名或密码错误！%s : %s'%(username,passwd))
#             if user:
#                 return HttpResponse("登陆成功")
#     else:
#         form = PeopleForm()
#     return render(request, 'people/login3.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = PeopleForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return HttpResponse('注册成功！')
#     else:
#         form = PeopleForm()
#     return render(request, 'people/register.html', {'form': form})
