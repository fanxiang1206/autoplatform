from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def model_list(request):
    return render(request,'model_list.html')