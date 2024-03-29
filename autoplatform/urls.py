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
from django.contrib import admin
from django.urls import path,include
from user import views

from jsdemo import views as js_views

urlpatterns = [

    path('admin/', admin.site.urls),
    # jquery学习
    path('js/', js_views.jisuan),
    path('js_demo/', js_views.js_demo),

    # 登录
    path('login/', views.login),
    path('', views.login),
    path('accounts/login/', views.login),
    path('logout/', views.logout),
    # 项目
    path('project/', include('project.urls')),
    # 模块
    path('module/', include('module.urls')),
    # 用例
    path('case/', include('case.urls')),

]
