from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project.models import Project
from django.http import HttpResponseRedirect
# Create your views here.


@login_required
def list(request):

    projects = Project.objects.all()
    return render(request, 'project.html', {"projects":projects,"type":"list"})


@login_required
def add(request):

    if request.method == "GET":
        return render(request, 'project.html',{"type":"add"})
    else:
        name = request.POST.get("name","")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")

        Project.objects.create(name=name,describe=describe,status=status)

        return HttpResponseRedirect('/project/list/')


@login_required
def update(request,pid):

    if request.method == "GET":
        project = Project.objects.get(id=pid)
        return render(request, 'project.html',{"project":project,"type":"update"})

    else:
        name = request.POST.get("name","")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")

        p = Project.objects.get(id=pid)
        p.name = name
        p.describe = describe
        p.status = status
        p.save()
        return HttpResponseRedirect('/project/list/')

    return


@login_required
def delete(request,pid):

    Project.objects.get(id=pid).delete()
    return HttpResponseRedirect('/project/list/')