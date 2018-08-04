# coding=utf-8
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ResourceInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="资源名称")
    code = models.CharField(max_length=50, verbose_name="资源编号")
    format = models.IntegerField(choices=(("1", "视频"), ("2", "h5资源包")), verbose_name="资源类型") #, ("3", "链接"), ("4", "文档") 暂不实现
    download = models.FileField(
        upload_to="resource/%Y/%m", verbose_name="资源文件", max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "资源文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CourseInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="课程名称")
    code = models.CharField(max_length=50, verbose_name="课程编号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CourseSection(models.Model):
    course = models.ForeignKey(CourseInfo, verbose_name="课程")
    resource = models.ForeignKey(ResourceInfo, verbose_name="资源")
    name = models.CharField(max_length=100, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
