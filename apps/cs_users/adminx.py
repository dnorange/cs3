# coding=utf-8
import xadmin
from xadmin import views
from django.core.exceptions import ObjectDoesNotExist

from .models import UserProfile


# try:
#     UserProfile.objects.get(username="cq")
# except ObjectDoesNotExist:
#     UserProfile.objects.create_superuser("cq", "chenqing001@189.cn", "admin123")


class BaseSetting(object):
    enable_themes = True  # 将隐藏的主题属性显现
    use_bootswatch = True  # 设置后才有很多主题可用


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = u"内容服务器3.0"
    site_footer = u"copyright 上海颐为网络科技有限公司"
    # menu_style = "accordion"  # 将各app的model折叠起来


xadmin.site.register(views.CommAdminView, GlobalSettings)  # 注册全局设定
