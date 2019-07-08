from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def jisuan(request):

    # num1 = request.GET.get("num1")
    # num2 = request.GET.get("num2")
    # # return HttpResponse(int(num1)+int(num2))
    # return JsonResponse({
    #     "sum":int(num1)+int(num2),
    #     "msg":"success"
    # }
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    print(num1)

    # return HttpResponse(int(num1)+int(num2))
    return JsonResponse({
        "sum": int(num1) + int(num2),
        "msg": "success"
    })

def js_demo(request):
    return render(request,'js_demo.html')