"""shangGuiGu URL Configuration

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
from django.urls import path,include,re_path
from orgs import views
urlpatterns = [
    # path(r'^user_register/$', user_register, name='user_register'),
    path('org_list/', views.org_list, name='org_list'),
    # 机构详情页-机构首页
    re_path('org_detail/(\d+)/$', views.org_detail, name='org_detail'),
    # 机构详情页-机构课程
    re_path('org_detail_course/(\d+)/$', views.org_detail_course, name='org_detail_course'),
    # 机构详情页-机构介绍
    re_path('org_detail_desc/(\d+)/$', views.org_detail_desc, name='org_detail_desc'),
# 机构详情页-机构讲师
    re_path('org_detail_teacher/(\d+)/$', views.org_detail_teacher, name='org_detail_teacher'),

    # 讲师列表
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    # 讲师详情页
    re_path('teacher_detail/(\d+)/$', views.teacher_detail, name='teacher_detail'),
]
