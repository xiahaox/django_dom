from user.models import EmailVerifyCode
from random import randrange
from django.core.mail import send_mail
from shangGuiGu.settings import EMAIL_FROM

# 获取随机验证码
def get_random_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += code_source[randrange(0, len(code_source)-1)]
    return code

def send_email_code(email, send_type):
    # 1、创建邮箱验证码对象保存数据库用来以后做对比
    code = get_random_code(8)
    a = EmailVerifyCode()
    print(EmailVerifyCode())
    a.email = email
    a.send_type = send_type
    a.code = code
    a.save()
    # 2、发邮件
    if send_type == 1:
        send_title = '欢迎注册谷粒教育网站：'
        send_body = '请点击以下链接进行激活，激活您的账号：\n http://127.0.0.1:8000/users/user_active/' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])
    elif send_type == 2:
        send_title = '谷粒教育重置密码系统：'
        send_body = '请点击以下链接重置您的密码：\n http://127.0.0.1:8000/users/user_reset/' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])