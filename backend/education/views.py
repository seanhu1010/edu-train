from rest_framework import viewsets
from .models import Student, Teacher, LessonTime, Course, Fee, Enrollment, Attendance
from .serializers import StudentSerializer, TeacherSerializer, LessonTimeSerializer, CourseSerializer, FeeSerializer, \
    EnrollmentSerializer, AttendanceSerializer


# 学员信息视图
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  # 从数据库中获取所有学员信息
    serializer_class = StudentSerializer  # 使用StudentSerializer进行序列化


# 老师信息视图
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()  # 从数据库中获取所有老师信息
    serializer_class = TeacherSerializer  # 使用TeacherSerializer进行序列化


# 上课时间信息视图
class LessonTimeViewSet(viewsets.ModelViewSet):
    queryset = LessonTime.objects.all()  # 从数据库中获取所有上课时间信息视图
    serializer_class = LessonTimeSerializer  # 使用LessonTimeSerializer进行序列化


# 课程信息视图
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()  # 从数据库中获取所有课程信息
    serializer_class = CourseSerializer  # 使用CourseSerializer进行序列化


# 费用信息视图
class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()  # 从数据库中获取所有费用信息
    serializer_class = FeeSerializer  # 使用FeeSerializer进行序列化


# 学员选课关系视图
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()  # 从数据库中获取所有选课关系信息
    serializer_class = EnrollmentSerializer  # 使用EnrollmentSerializer进行序列化


# 签到记录视图
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()  # 从数据库中获取所有签到记录信息
    serializer_class = AttendanceSerializer  # 使用AttendanceSerializer进行序列化
