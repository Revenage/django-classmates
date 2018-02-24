from django.contrib import admin

from .models import Teacher, Subject, Grade, Student

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Student)