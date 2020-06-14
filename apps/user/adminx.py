import xadmin
from .models import BannerInfo, EmailVerifyCode
from xadmin import views
# 主题
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True

class CommonXadminSetting(object):
    site_title = '谷粒教育后台管理系统'
    site_footer = '尚硅谷it教育'
    # menu_style = 'accordion' # 左边模块折叠

# 轮播图
class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']

# 验证码
class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 注册全局样式类
xadmin.site.register(views.CommAdminView, CommonXadminSetting)