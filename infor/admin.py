# -*- coding: utf-8 -*-
from PIL import Image
import django

from django.contrib import admin
from django.contrib import messages
from infor.models import Student, Hclass


# Register your models here.


class StudentInline(admin.StackedInline):
    model = Student
    extra = 1

class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['class_name']}),
    ]

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['whichclass__class_name', 'name']
    list_display = ('name', 'whichclass', 'mobile')
    list_filter = ['whichclass']

class ReplyAdmin(admin.ModelAdmin):
    search_fields = ['reply_id']

# Register your models here.
admin.site.register(Hclass, ClassAdmin)
admin.site.register(Student, StudentAdmin)

django.contrib.admin.AdminSite.site_header = u'和君八届毕业生基本信息收集系统'
django.contrib.admin.AdminSite.site_title = u'和君八届毕业生基本信息收集系统'