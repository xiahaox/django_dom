from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, logout, login
from .models import UserProfile, EmailVerifyCode
from django.db.models import Q
from utils.send_mail_tool import send_email_code
from user.models import EmailVerifyCode
from django.http import JsonResponse
# Create your views here.


# < !--  { % url
# 'user:user_logout' %}  { % url
# 'user:user_register' %}  { % url
# 'user:user_login' %}  -->
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm() # 是为了使用验证码
        # print(user_register_form.captcha )
        return render(request, 'register.html', {
            'user_register_form': user_register_form
        })
    else :
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            # 先查找用户表中是否有这个用户
            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg': '用户已经存在'
                })
            else:
                a = UserProfile()
                a.username = email
                a.set_password(password)
                a.email = email
                a.save()
                send_email_code(email, 1)
                return HttpResponse('请尽快前往您的邮箱激活，否则无法登陆')
                # return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })
    #     return HttpResponse('请尽快前往您的邮箱激活，否则无法登陆')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            # authenticate验证的就是username的字段
            user = authenticate(username=email, password=password)
            if user:
                if user.is_start:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('请去您的邮箱激活，否则无法登陆')
            else:
                return render(request, 'login.html',{
                    'msg': '邮箱或者密码有误'
                })
        else:
            print(111)
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })

def user_activate(request,code):
    if code:
        email_ver_list = EmailVerifyCode.objects.filter(code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            print(email_ver)
            email = email_ver.email
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                user = user_list[0]
                user.is_start = True
                user.save()
                return redirect(reverse('user:user_login'))
            else:
                pass
        else:
            pass
    else:
        pass

def user_logout(request):
    print(request)
    return redirect(reverse('index'))

def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request, 'forgetpwd.html', {
            'user_forget_form': user_forget_form
        })
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            # print(user_forget_form.cleaned_data)
            email = user_forget_form.cleaned_data['email']
            user_list = UserProfile.objects.filter(email=email)
            print(user_list)
            if user_list:
                # send_email_code(email, 2)
                return HttpResponse('请尽快去您的邮箱重置密码')
            else:
                return render(request, 'forgetpwd.html',{
                    'msg': '用户不存在'
                })
        else:
            return render(request, 'forgetpwd.html', {
                'user_forget_form': user_forget_form
            })

def user_reset(request,code):
    print(code)
    if request.method == 'GET':
        return render(request, 'password_reset.html', {
            'code': code
        })
    else:
        user_reset_form = UserResetForm(request.POST)
        if user_reset_form.is_valid():
            password = user_reset_form.cleaned_data['password']
            password1 = user_reset_form.cleaned_data['password1']
            if password == password1:
                print('222')
                email_var_list = EmailVerifyCode.objects.filter(code=code)
                if email_var_list:
                    print('333')
                    email_var = email_var_list[0]
                    email = email_var.email
                    print(email)
                    user_list = UserProfile.objects.filter(email=email)
                    if user_list:
                        print('444')
                        user = user_list[0]
                        print(user.email)
                        user.set_password(password)
                        user.save()
                        return redirect(reverse('users:user_login'))
                    else:
                        print('555')
                        pass
                else:
                    print('666')
                    pass
            else:
                print('777')
                return render(request, 'password_reset.html', {
                    'msg': '两次密码不一致',
                    'code': code
                })
        else:
            print('888')
            return render(request, 'password_reset.html',{
                'user_reset_form': 'user_reset_form',
                'code': code
            })


# 个人用户中心-个人资料
def user_info(requests):
    return render(requests,'users/usercenter-info.html')



# 个人用户中心-个人资料-修改用户头像
def user_changeimage(request):
    # request.POST 验证图片文件以外的其他内容
    # request.FILES 验证图片文件
    # instance 指明实例是什么,做修改的时候,我们需要知道给哪个对象实例进行修改
    # instance 如果不指明,就会当做创建对象去执行,而我们只有一个图片,就会报错
    user_changeimage_form = UserChangeimageForm(request.POST,request.FILES,instance=request.user)
    if user_changeimage_form.is_valid():
        user_changeimage_form.save(commit=True)
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'fail'})

# 个人用户中心-个人资料-修改用户信息
def user_changeinfo(request):
    user_changeinfo_form = UserChangeInfoForm(request.POST,instance=request.user)
    if user_changeinfo_form.is_valid():
        user_changeinfo_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'修改成功'})
    else:
        return JsonResponse({'status':'fail','msg':'修改失败'})

# 个人用户中心-个人资料-修改用户邮箱-发送验证码
def user_changeemail(request):
    user_changeemail_form = UserChangeEmailForm(request.POST)
    if user_changeemail_form.is_valid():  # 验证输入的新邮箱数据
        email = user_changeemail_form.cleaned_data['email']  # 获取新邮箱

        email_list = UserProfile.objects.filter(Q(email=email)|Q(username=email))  # 查询新的邮箱是否在数据库表中
        if email_list:  # 说明这个新邮箱已在数据库中,则无法使用
            return JsonResponse({'status':'fail','msg':'此邮箱已被绑定'})
        else:  # 说明这个新邮箱不在数据库中,可以使用
            # 在发送邮件验证码之前,应该去邮箱验证码表中查找,看看之前有没有往当前这个新邮箱发送过修改邮箱这个类型的验证码
            email_ver_list = EmailVerifyCode.objects.filter(email=email,send_type=3)
            if email_ver_list:  # 说明发送过验证码,那么需要获取到新近发送这个一个验证码时间
                email_ver = email_ver_list.order_by('-add_time')[0]
                # 判断当前时间与最近发送的验证码添加时间之差
                if (datetime.now() - email_ver.add_time).seconds > 60:  # 表示距离上次发送验证码时间大于60秒,可以再次发送
                    send_mail_code(email,3)
                    # 如果我们重新发送了新的验证码,那么以前最近发的就可以清楚掉
                    email_ver.delete()
                    return JsonResponse({'status':'ok','msg':'请去你的新邮箱中获取验证码'})
                else:  # 小于60秒,不需要再次发送验证码
                    return JsonResponse({'status':'fail','msg':'请不要重发发送验证码,60秒后再试'})
            else:  # 未发送过验证码
                send_mail_code(email,3)
                return JsonResponse({'status':'ok','msg':'请去你的新邮箱中获取验证码'})
    else:  # 输入的邮箱信息未通过验证
        return JsonResponse({'status':'fail','msg':'输入邮箱信息错误'})

# 个人用户中心-个人资料-修改用户邮箱-完成
def user_resetemail(request):

    user_resetemail_form = UserResetEmailForm(request.POST)
    if user_resetemail_form.is_valid():
        email = user_resetemail_form.cleaned_data['email']
        code = user_resetemail_form.cleaned_data['code']

        email_ver_list = EmailVerifyCode.objects.filter(email=email,code=code,)  # 查找新邮箱与新邮箱验证码是否在数据表中存在这个对象
        if email_ver_list:
            email_ver = email_ver_list[0]
            if (datetime.now() - email_ver.add_time).seconds < 60:  # 说明验证码还未过期
                request.user.username = email
                request.user.email = email
                request.user.save()
                return JsonResponse({'status':'ok','msg':'新邮箱修改成功'})
            else:  # 大于60秒
                return JsonResponse({'status':'fail','msg':'验证码已过期,请重新发送验证码'})
        else:  # 未在数据库表中查找到数据
            return JsonResponse({'status':'fail','msg':'邮箱或验证码输入错误'})
    else:  # 数据未通过验证
        return JsonResponse({'status':'fail','msg':'邮箱或验证码不合法'})

# 个人用户中心-我的课程
def user_course(request):

    # 根据登陆用户信息 查找 用户课程表的数据
    usercourse_list = request.user.usercourse_set.all()
    # 在根据用户课程表 信息 获取到所有的 课程信息
    course_list = [usercourse.study_course for usercourse in usercourse_list]

    return render(request,'users/usercenter-mycourse.html',{
        'course_list':course_list,
    })

# 个人用户中心-我的收藏(机构1)
def user_loveorg(request):

    # 根据登陆用户查找 用户收藏表的所有信息  然后在根据 类型 筛选出收藏信息(机构)
    # userloveorg_list = request.user.userlove_set.all()
    # 直接从 用户收藏表 中根据登陆用户于类型字典  查找到需要的收藏信息(机构)
    userloveorg_list = UserLove.objects.filter(love_man=request.user,love_type=1,love_status=True)

    # 根据收藏信息获取到收藏id(机构)
    org_ids = [userloveorg.love_id for userloveorg in  userloveorg_list]

    # 根据收藏id查找到机构信息
    org_list = OrgInfo.objects.filter(id__in=org_ids)

    return render(request,'users/usercenter-fav-org.html',{
        'org_list':org_list,
    })

# 个人用户中心-我的收藏(讲师3)
def user_loveteacher(request):

    # 根据登陆用户查找 用户收藏表的所有信息  然后在根据 类型 筛选出收藏信息(讲师)
    # userloveteacher_list = request.user.userlove_set.all()
    # 直接从 用户收藏表 中根据登陆用户于类型字典  查找到需要的收藏信息(讲师)
    userloveteacher_list = UserLove.objects.filter(love_man=request.user,love_type=3,love_status=True)

    # 根据收藏信息获取到收藏id(讲师)
    teacher_ids = [userloveteacher.love_id for userloveteacher in  userloveteacher_list]

    # 根据收藏id查找到机构信息
    teacher_list = TeacherInfo.objects.filter(id__in=teacher_ids)

    return render(request,'users/usercenter-fav-teacher.html',{
        'teacher_list':teacher_list,
    })

# 个人用户中心-我的收藏(课程2)
def user_lovecourse(request):

    # 根据登陆用户查找 用户收藏表的所有信息  然后在根据 类型 筛选出收藏信息(课程)
    # userlovecourse_list = request.user.userlove_set.all()
    # 直接从 用户收藏表 中根据登陆用户于类型字典  查找到需要的收藏信息(课程)
    userlovecourse_list = UserLove.objects.filter(love_man=request.user,love_type=2,love_status=True)

    # 根据收藏信息获取到收藏id(课程)
    course_ids = [userlovecourse.love_id for userlovecourse in  userlovecourse_list]

    # 根据收藏id查找到机构信息
    course_list = CourseInfo.objects.filter(id__in=course_ids)

    return render(request,'users/usercenter-fav-course.html',{
        'course_list':course_list,
    })

# 个人用户中心-我的消息
def user_message(request):

    msg_list = UserMessage.objects.filter(message_man=request.user.id)

    return render(request,'users/usercenter-message.html',{
        'msg_list':msg_list,
    })

# 个人用户中心-我的消息-未读消息变成已读消息
def user_deletemessage(request):

    msgid = request.GET.get('msgid','')  # ajax请求传递过来未读消息的id
    if msgid:
        userMessage = UserMessage.objects.filter(id=int(msgid))[0]  # 根据消息id从消息表查找消息对象
        userMessage.message_status = True  # 修改未读消息的状态False(默认)为True
        userMessage.save()
        return JsonResponse({'status':'ok','msg':'已读'})
    else:
        return JsonResponse({'status':'fail','msg':'读取失败'})


# 404
def handler_404(request):
    return render(request,'handler_404.html')
# 500
def handler_500(request):
    return render(request,'handler_500.html')