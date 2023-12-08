from django.contrib import admin
from .models import Student, Teacher,LessonTime, Course, Fee, Enrollment, Attendance

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(LessonTime)
admin.site.register(Course)
admin.site.register(Fee)
admin.site.register(Enrollment)
admin.site.register(Attendance)
