import xadmin
from .models import *

class CourseInfoXadmin(object):
    list_display = ['image', 'name', 'study_time', 'study_num', 'level', 'love_num', 'click_num', 'category', 'orginfo', 'teacherinfo']
    model_icon = 'fa fa-address-book'

# 章节表
class LessonInfoXadmin(object):
    list_display = ['name', 'courseinfo']
    model_icon = 'fa fa-bath'

# 视频信息
class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'lessoninfo']
    model_icon = 'fa fa-bath'

# 资源表
class SourceInfoXadmin(object):
    list_display = ['name', 'download', 'courseinfo']
    model_icon = 'fa fa-grav'

xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)