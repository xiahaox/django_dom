import xadmin
from .models import *

# 城市信息
class CityInfoXadmin(object):
    list_play = ['name', 'add_time']

# 机构信息
class OrgInfoXadmin(object):
    list_play = ['image', 'name', 'course_num', 'study_num', 'love_num', 'click_num', 'category', 'cityinfo']

# 教师表
class TeacherInfoXadmin(object):
    list_play = ['image', 'name', 'work_year', 'work_postion', 'age', 'gender', 'love_num', 'click_num']

xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgInfo, OrgInfoXadmin)
xadmin.site.register(TeacherInfo, TeacherInfoXadmin)