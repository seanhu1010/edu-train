from django.contrib import admin
from .models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, Course, \
    FeeDetail, PaymentRecord, Attendance

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(DictionaryData)
admin.site.register(Avatar)
admin.site.register(Parent)
admin.site.register(Dropout)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Fee)
admin.site.register(Period)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(FeeDetail)
admin.site.register(PaymentRecord)
admin.site.register(Attendance)
