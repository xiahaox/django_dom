from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
# null=True 表示在数据库里面 这些字段是可以为空的
# blank=True 表示在页面表单里 这些字段是可以为空的
# 用户表
class UserProfile(AbstractUser):
    image= models.ImageField(upload_to='user/',max_length = 200,verbose_name='用户头像', blank = True, null = True)
    nick_name= models.CharField(max_length = 20,verbose_name='用户昵称', blank = True, null = True)
    birthday=models.DateTimeField(verbose_name='用户生日', blank = True, null = True)
    gender=models.CharField(verbose_name='用户生日',default='girl', max_length = 10,choices=(('girl','女'),('body','男')))
    address = models.CharField(max_length=200, verbose_name='用户地址', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='用户手机', blank=True, null=True)
    is_start = models.BooleanField(default=False, verbose_name='是否激活')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    def __str__(self):
        return self.username
    class Meta:
        verbose_name ='用户信息'
        verbose_name_plural=verbose_name

# 轮播图
class BannerInfo(models.Model):
    image = models.ImageField(upload_to='banner/', verbose_name='轮播图片', max_length=200)
    url = models.URLField(default='http://www.atguigu.com', max_length=200, verbose_name='图片链接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = '轮播图信息'
        verbose_name_plural = verbose_name


# 验证码
class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=200, verbose_name='验证码邮箱')
    send_type = models.IntegerField(choices=((1, 'register'), (2, 'forget'), (3, 'change')), verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name