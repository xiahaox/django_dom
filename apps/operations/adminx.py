import xadmin
from .models import *

# 用户咨询表
class UserAskXadmin(object):
    list_display = ['name', 'phone', 'course']

# 用户收藏表
class UserLoveXadmin(object):
    list_display = ['love_man', 'love_id', 'love_type', 'love_statu']

# 用户学习课程表
class UserCourseXadmin(object):
    list_display = ['study_man', 'study_course']


# 用户评论表
class UserCommentXadmin(object):
    list_display = ['comment_man', 'comment_course', 'comment_content']

# 用户消息表
class UserMessageXadmin(object):
    list_display = ['message_man', 'message_content', 'message_status']

xadmin.site.register(UserAsk, UserAskXadmin)
xadmin.site.register(UserLove, UserLoveXadmin)
xadmin.site.register(UserCourse, UserCourseXadmin)
xadmin.site.register(UserComment, UserCommentXadmin)
xadmin.site.register(UserMessage, UserMessageXadmin)