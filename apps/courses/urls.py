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
from django.urls import path,include,re_path
from courses import views

urlpatterns = [
    # 公开课列表
    path('course_list/',views.course_list, name='course_list'),
    # 公开课课程详情
    re_path('course_detail/(\d+)/$',views.course_detail, name='course_detail'),
    # 公开课课程视频-章节
    re_path('course_video/(\d+)/$',views.course_video, name='course_video'),
    # 公开课课程视频-评论
    re_path('course_comment/(\d+)/$',views.course_comment, name='course_comment'),
]
