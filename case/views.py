from django.shortcuts import render
from case.httpclient import httpclient
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
    req_method = request.POST.get("req_method"),
    reg_header = request.POST.get("reg_header",""),
    req_type = request.POST.get("req_type",""),
    reg_param = request.POST.get("reg_param","")

    client = httpclient(url=reg_url,method=req_method[0],body_type=req_type[0])

    if reg_url == '' or reg_url is None:

        return JsonResponse({
            "errocde": 1001,
            "errdesc": "失败,请求地址不能为空！！！",
            "result": ""
        })
    #
    # print("3333")
    # print(reg_header)
    # print(reg_header[0])
    #
    # print("4444")
    client.set_headers(json.loads(reg_header[0]))

    # if reg_param[0] != '' and reg_param[0] is not None:
    #     client.set_params(reg_param)

    client.send()

    print(type(client.res.json()))

    return JsonResponse({
        "errcode":0,
        "errdesc":"成功",
        "data":client.res.json()
    })
