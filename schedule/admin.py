from django.contrib import admin

from .models import Grade, Subject, Teacher, SheduleItem, ClassRoom, LessonTime

admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(SheduleItem)
admin.site.register(ClassRoom)
admin.site.register(LessonTime)
