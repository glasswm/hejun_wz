# -*- coding: utf-8 -*-
from PIL import Image
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

@deconstructible
class ImageValidator(object):
    code = 'invalid_size'

    def __init__(self, code=None, whitelist=None):
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not value:
            raise ValidationError(u'未上传图片', code=self.code)
        else:
            if value.size > 2*1024*1024:
                raise ValidationError(u'图片大小不应超过2MB', code=self.code)
            else:
                image = Image.open(value)
                if image.size[0]!=300 or image.size[1]!=300:
                    raise ValidationError(u'图片尺寸应为: 300x300', code=self.code)


class MyImageField(models.ImageField):
    default_validators = [ImageValidator()]

    def __init__(self, *args, **kwargs):
        super(MyImageField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MyImageField, self).deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs


class Hclass(models.Model):
    class_name = models.CharField(u'班级名称', max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.class_name

    class Meta:
        verbose_name = u'班级'
        verbose_name_plural = u'班级'

class Student(models.Model):

    COLLEDGE = 'CO'
    BACHELOR = 'BA'
    MASTER = 'MA'
    DOCTOR = 'DO'
    OTHER = 'OT'
    EDUCATION_BACKGROUD_CHOICES = (
        (COLLEDGE, u'大专'),
        (BACHELOR, u'本科'),
        (MASTER, u'硕士'),
        (DOCTOR, u'博士'),
        (OTHER, u'其他'),
    )

    name = models.CharField(u'姓名', max_length=10, null=False)
    whichclass = models.ForeignKey(Hclass, verbose_name=u'所属班级', related_name='student', null=False)
    ismonitor = models.BooleanField(u'是否为班长', null=False, default=False)
    education = models.CharField(u'最高学历', max_length=2, choices=EDUCATION_BACKGROUD_CHOICES, default=MASTER, null=False)
    university_company = models.CharField(u'就读院校/工作单位', max_length=40, null=False)
    mobile = models.CharField(u'手机号', max_length=30, null=False, unique=True)
    email = models.EmailField(u'邮箱', null=False)
    wechat = models.CharField(u'微信号', max_length=20, null=False)
    dream = models.TextField(u'我有一个梦想', max_length=150, null=False, help_text=u'不超过150个汉字')
    want_say = models.TextField(u'一句想说的话', max_length=30, null=False, help_text=u'不超过30个汉字')
    photo = MyImageField(u'个人照片', null=False, upload_to='photos', help_text=u'图片格式应为jpg或png，尺寸为300x300，文件大小不超过2MB')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = u'学生'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        #fields = ['name', 'whichclass', 'education']


if __name__ == '__main__':
    pass