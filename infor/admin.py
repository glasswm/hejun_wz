from django.contrib import admin
from infor.models import Student, Hclass


# Register your models here.


class StudentInline(admin.StackedInline):
    model = Student
    extra = 3

class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['class_name']}),
    ]
    inlines = [StudentInline]

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['whichclass__class_name', 'name']
    list_display = ('name', 'whichclass', 'mobile')

class ReplyAdmin(admin.ModelAdmin):
    search_fields = ['reply_id']

# Register your models here.
admin.site.register(Hclass, ClassAdmin)
admin.site.register(Student, StudentAdmin)