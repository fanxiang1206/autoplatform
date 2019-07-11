from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from module.models import Module
from project.models import Project
from django.http import HttpResponseRedirect
# Create your views here.


@login_required
def list(request):

    modules = Module.objects.all()
    return render(request, 'module.html', {"modules":modules,"type":"list"})


@login_required
def add(request):

    if request.method == "GET":
        projects = Project.objects.all()
        return render(request, 'module.html',{"projects":projects,"type":"add"})
    else:
        name = request.POST.get("name","")
        describe = request.POST.get("describe", "")
        project_id = request.POST.get("project_id", "")

        Module.objects.create(name=name,describe=describe,project_id=project_id)

        return HttpResponseRedirect('/module/list/')


@login_required
def update(request,pid):

    if request.method == "GET":
        module = Module.objects.get(id=pid)
        projects = Project.objects.all()
        return render(request, 'module.html',{"module":module,"projects":projects,"type":"update"})

    else:
        name = request.POST.get("name","")
        describe = request.POST.get("describe", "")
        project_id = request.POST.get("project_id", "")

        p = Module.objects.get(id=pid)
        p.name = name
        p.describe = describe
        p.project_id = project_id
        p.save()
        return HttpResponseRedirect('/module/list/')

    return


@login_required
def delete(request,pid):

    Module.objects.get(id=pid).delete()
    return HttpResponseRedirect('/module/list/')