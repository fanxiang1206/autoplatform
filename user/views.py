from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):

    if request.method =='GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/project_list/')
        else:
            context = {
                "msg": "用户名或者密码不正确！！！"
            }
            return render(request, 'login.html', context=context)

@login_required
def logout(request):

    auth.logout(request)
    return  HttpResponseRedirect('/login/')
