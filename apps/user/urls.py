from django.urls import path, include

from django.contrib import admin
from django.urls import path, include, re_path
from user import views
from user.views import *

urlpatterns = [
     # 注册
     path('user_register/', user_register, name='user_register'),
     # # 登陆
     path('user_login/', user_login, name='user_login'),
     # # 注销
     path('user_logout/',user_logout, name='user_logout'),
     # # 激活邮箱验证码
     re_path('user_active/(\w+)', user_activate, name='user_activate'),
     # 忘记密码
     path('user_forget/', user_forget, name='user_forget'),
     # # 激活邮箱验证码
     re_path('user_reset/(\w+)/$', user_reset, name='user_reset'),
     # 个人用户中心-个人资料
     path('user_info/', user_info, name='user_info'),

     # # 个人用户中心-个人资料-修改用户头像
     path('user_changeimage/', views.user_changeimage, name='user_changeimage'),
     # 个人用户中心-个人资料-修改用户信息
     path('user_changeinfo/', views.user_changeinfo, name='user_changeinfo'),
     # 个人用户中心-个人资料-修改用户邮箱-发送验证码
     path('user_changeemail/', views.user_changeemail, name='user_changeemail'),
     # 个人用户中心-个人资料-修改用户邮箱-完成
     path('user_resetemail/', views.user_resetemail, name='user_resetemail'),
     # 个人用户中心-我的课程
     path('user_course/', views.user_course, name='user_course'),
     # 个人用户中心-我的收藏(机构1)
     path('user_loveorg/', views.user_loveorg, name='user_loveorg'),
     # 个人用户中心-我的收藏(讲师3)
     path('user_loveteacher/', views.user_loveteacher, name='user_loveteacher'),
     # 个人用户中心-我的收藏(课程2)
     path('user_lovecourse/', views.user_lovecourse, name='user_lovecourse'),
     # 个人用户中心-我的消息
     path('user_message/', views.user_message, name='user_message'),
     # 个人用户中心-我的消息-未读消息变成已读消息
     path('user_deletemessage/', views.user_deletemessage, name='user_deletemessage'),
]
