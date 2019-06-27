from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    name = request.GET.get("name","")
    return HttpResponse("测试成功!!!!!"+name)