# coding=utf-8
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProfile(AbstractUser):  # 继承Django自身的AbstractUser,沿用默认字段
    nick_name = models.CharField(
        max_length=50, verbose_name=u"昵称", default="")  # 增加昵称字段, 默认为空""
    birthday = models.DateField(
        verbose_name=u"生日", null=True, blank=True)  # 增加生日字段, 允许null与空
    gender = models.CharField(
        choices=(("Male", "男"), ("female", "女")),
        max_length=6)  # 增加性别字段, 使用了choices选项
    address = models.CharField(max_length=100, default="")  # 增加地址字段
    mobile = models.CharField(max_length=11, null=True, blank=True)  # 增加手机字段
    image = models.ImageField(
        upload_to="image/%Y/%m", default="image/default.png", max_length=100
    )  # 增加用户头像字段, image/%Y/%m代表上传时按年月文件夹进行, default设置的是默认头像路径

    class Meta:
        verbose_name = "用户信息"  # 设置UserProfle这个类的别名
        verbose_name_plural = verbose_name  # 设置别名的复数形式

    def __str__(self):
        return self.username  # 当使用print打印时, 把继承的username字段打印出来
