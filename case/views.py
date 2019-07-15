from django.shortcuts import render
from case.httpclient import httpclient
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from project.models import Project
from module.models import Module
from case.models import Case

# Create your views here.

#case列表查询
@login_required
def list(request):

    modules = Module.objects.all()

    cases_list = Case.objects.all()

    paginator = Paginator(cases_list, 5)

    page = request.GET.get('page')

    try:

        cases = paginator.page(page)  # contacts为Page对象！

    except PageNotAnInteger:

        cases = paginator.page(1)

    except EmptyPage:

        cases = paginator.page(paginator.num_pages)


    return render(request,'case.html',{"modules":modules,"cases":cases,"type":"list"})

#添加测试用例
@login_required
def add(request):

    projects = Project.objects.all()

    return render(request,'case.html',{"type":"add","projects":projects})

#根据项目id查询下属模块
@login_required
def queryModule(request):

    module_list = {}
    req_project = request.GET.get("req_project","")
    modules = Module.objects.filter(project_id=req_project)
    for module in modules:
        module_list[module.id] = module.name

    return HttpResponse(json.dumps(module_list))


#调试和发送测试用例请求
@login_required
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

    try:
        client.send()
    except Exception as e:
        print("异常信息为：",str(e))
        return HttpResponse(str(e))


    # print(client.res.json())

    # {"x-qp-appid": "21001", "x-qp-gid": "1", "x-qp-userid": "1"}

    return HttpResponse(str(client.res.json()))

#测试用例断言
@login_required
@csrf_exempt
def req_assert(request):

    req_assert_type = request.POST.get("req_assert_type","")
    req_assert_param = request.POST.get("req_assert_param","")
    req_result = request.POST.get("req_result","")

    if req_assert_param == "":

        return HttpResponse("预期结果不能为空！！！")

    if req_result == "":

        return HttpResponse("实际结果不能为空！！！")

    if req_assert_type == "contains":

        if req_assert_param in req_result:

            return HttpResponse("断言成功！！！")
        else:

            return HttpResponse("断言失败！！！")

    elif req_assert_type == "equals":

        if req_assert_param == req_result:

            return HttpResponse("断言成功！！！")
        else:

            return HttpResponse("断言失败！！！")
    else:

        return HttpResponse("断言类型错误,错误的类型为："+req_assert_type)


#保存测试用例
@login_required
@csrf_exempt
def save(request):

    msg = "用例保存成功！！！"

    req_name = request.POST.get("req_name","")
    reg_url = request.POST.get("reg_url","")
    req_method = request.POST.get("req_method","")
    reg_header = request.POST.get("reg_header","")
    req_type = request.POST.get("req_type","")
    reg_param = request.POST.get("reg_param","")
    req_assert_type = request.POST.get("req_assert_type","")
    req_assert_param = request.POST.get("req_assert_param","")
    req_module = request.POST.get("req_module","")

    try:
        Case.objects.create(name=req_name,
                            url=reg_url,
                            method=req_method,
                            header=reg_header,
                            param_type=req_type,
                            params=reg_param,
                            assert_type=req_assert_type,
                            assert_params=req_assert_param,
                            module_id=req_module)
    except Exception as e:

        print("异常信息为：",str(e))
        msg = "用例保存失败，失败原因为{error}".format(str(e))


    return JsonResponse({
        "msg":msg
    })



#删除测试用例
@login_required
def delete(request,pid):

    Case.objects.get(id=pid).delete()

    return HttpResponseRedirect('/case/list/')

#查询测试用例
@login_required
def queryCase(request,pid):

    if request.method == "GET":

        projects = Project.objects.all()

        case = Case.objects.get(id=pid)

        if case:

            module = Module.objects.get(id=case.module_id)

            if module:

                project_single = Project.objects.get(id=module.project_id)

                modules = Module.objects.filter(project=project_single)

                return render(request, 'case.html',{"modules":modules,
                                                    "project_single":project_single,
                                                    "case": case,
                                                    "type":"update",
                                                    "projects":projects
                                                    })



#编辑测试用例
@login_required
@csrf_exempt
def update(request):

    msg = "用例编辑成功！！！"

    req_id = request.POST.get("req_id", "")
    req_name = request.POST.get("req_name", "")
    reg_url = request.POST.get("reg_url", "")
    req_method = request.POST.get("req_method", "")
    reg_header = request.POST.get("reg_header", "")
    req_type = request.POST.get("req_type", "")
    reg_param = request.POST.get("reg_param", "")
    req_assert_type = request.POST.get("req_assert_type", "")
    req_assert_param = request.POST.get("req_assert_param", "")
    req_module = request.POST.get("req_module", "")


    try:

        case = Case.objects.get(id=req_id)
        case.name = req_name
        case.url = reg_url
        case.method = req_method
        case.header = reg_header
        case.param_type = req_type
        case.params = reg_param
        case.assert_type = req_assert_type
        case.assert_params = req_assert_param
        case.module_id = req_module
        case.save()

    except Exception as e:

        print("异常信息为：", str(e))
        msg = "编辑用例失败，失败原因为{error}".format(str(e))

    return JsonResponse({
        "msg": msg
    })
