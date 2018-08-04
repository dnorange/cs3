# coding=utf-8
import xadmin

from .models import ResourceInfo
from .models import CourseInfo
# from .models import CourseSection


class ResourceAdmin(object):
    pass


class CourseAdmin(object):
    pass


class SectionAdmin(object):
    pass


xadmin.site.register(ResourceInfo, ResourceAdmin)
xadmin.site.register(CourseInfo, CourseAdmin)
# xadmin.site.register(CourseSection, SectionAdmin)