from django.shortcuts import render
from case.httpclient import httpclient
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.

def list(request):

    pass

    return render(request,'case.html',{"type":"list"})


def add(request):

    pass

    return render(request,'case.html',{"type":"add"})


@csrf_exempt
def debug(request):

    reg_url = request.POST.get("reg_url","")
    req_method = request.POST.get("req_method")
    reg_header = request.POST.get("reg_header","")
    req_type = request.POST.get("req_type","")
    reg_param = request.POST.get("reg_param","")

    #初始化httpclient对象
    client = httpclient(url=reg_url,method=req_method,body_type=req_type)

    if reg_url == '' or reg_url is None:

        return HttpResponse("请求的url不能为空！！！")

    if reg_header != '' and reg_header is not None:

        client.set_headers(json.loads(reg_header))

    if reg_param != '' and reg_param is not None:

        client.set_params(json.loads(reg_param))

    client.send()

    # print(client.res.json())

    # {"x-qp-appid": "21001", "x-qp-gid": "1", "x-qp-userid": "1"}

    return HttpResponse(str(client.res.json()))
