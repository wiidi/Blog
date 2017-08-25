from django.http import HttpResponse
from django.shortcuts import render
from people.models import People
from django import forms


class PeopleForm(forms.ModelForm):
    username = forms.CharField(label='账号', required=True)
    passwd = forms.CharField(label='密码', required=True, widget=forms.PasswordInput)

    class Meta:
        model = People
        fields = ('username', 'passwd')

def index(request):
    return render(request, 'index.html', {})

def login(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # passwd = form.changed_data['passwd']
            username = request.POST.get('username')
            passwd = request.POST.get('passwd')

            # username = form['username']
            # passwd = form['passwd']
            try:
                user = People.objects.get(username=username, passwd=passwd)
            except:
                return HttpResponse('用户名或密码错误！%s : %s'%(username,passwd))
            if user:
                return HttpResponse("登陆成功")
    else:
        form = PeopleForm()
    return render(request, 'people/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('注册成功！')
    else:
        form = PeopleForm()
    return render(request, 'people/register.html', {'form': form})


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
