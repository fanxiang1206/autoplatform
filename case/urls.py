"""autoplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from case import views


urlpatterns = [

    path('debug/', views.debug),
    path('req_assert/', views.req_assert),
    path('list/', views.list),
    path('add/', views.add),
    path('queryModule/', views.queryModule),
    path('save/', views.save),
    path('update/<int:pid>/', views.update),
    path('delete/<int:pid>/', views.delete),


]
