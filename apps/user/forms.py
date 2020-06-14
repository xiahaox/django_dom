from django import forms
from captcha.fields import CaptchaField
from user.models import UserProfile,EmailVerifyCode

class UserRegisterForm(forms.Form):
    # 自动验证是否是邮箱格式
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填写',
        'min_length': '密码至少3位',
        'max_length': '密码不能超过15位'
    })
    # 使用验证码
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

class UserLoginForm(forms.Form):
    # 自动验证是否是邮箱格式
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填写',
        'min_length': '密码至少3位',
        'max_length': '密码不能超过15位'
    })

class UserForgetForm(forms.Form):
    # 自动验证是否是邮箱格式
    email = forms.EmailField(required=True)
    # 使用验证码
    captcha = CaptchaField()

class UserResetForm(forms.Form):
    password = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填写',
        'min_length': '密码至少3位',
        'max_length': '密码不能超过15位'
    })
    password1 = forms.CharField(required=True, min_length=3, max_length=15, error_messages={
        'required': '密码必须填写',
        'min_length': '密码至少3位',
        'max_length': '密码不能超过15位'
    })




# 个人用户中心-修改用户信息
class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','birthday','gender','address','phone']

# 个人用户中心-修改用户头像
class UserChangeimageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


# 个人用户中心-修改用户邮箱-发送验证码
class UserChangeEmailForm(forms.ModelForm):
    class Meta:
        # model = UserProfile
        model = EmailVerifyCode
        fields = ['email']
