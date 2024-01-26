from rest_framework import viewsets
from .models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, Course, \
    FeeDetail, PaymentRecord, Attendance
from .serializers import DictionarySerializer, DictionaryDataSerializer, AvatarSerializer, ParentSerializer, \
    DropoutSerializer, TeacherSerializer, StudentSerializer, FeeSerializer, PeriodSerializer, LessonSerializer, \
    CourseSerializer, FeeDetailSerializer, PaymentRecordSerializer, AttendanceSerializer


# 字典表视图
class DictionaryViewSet(viewsets.ModelViewSet):
    # 从数据库中获取所有字典信息，按照id排序
    queryset = Dictionary.objects.all().order_by('id')
    serializer_class = DictionarySerializer


# 字典数据表视图
class DictionaryDataViewSet(viewsets.ModelViewSet):
    # 从数据库中获取所有字典信息，按照id排序
    queryset = DictionaryData.objects.all().order_by('id')
    serializer_class = DictionaryDataSerializer


# 头像表视图
class AvatarViewSet(viewsets.ModelViewSet):
    # 从数据库中获取所有字典信息，按照id排序
    queryset = Avatar.objects.all().order_by('-id')
    serializer_class = AvatarSerializer


# 家长表视图
class ParentViewSet(viewsets.ModelViewSet):
    # 从数据库中获取所有字典信息，按照id排序
    queryset = Parent.objects.all().order_by('-id')
    serializer_class = ParentSerializer


# 流失表视图
class DropoutViewSet(viewsets.ModelViewSet):
    queryset = Dropout.objects.all().order_by('-id')
    serializer_class = DropoutSerializer


# 学员信息视图
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')  # 从数据库中获取所有学员信息
    serializer_class = StudentSerializer  # 使用StudentSerializer进行序列化


# 老师信息视图
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')  # 从数据库中获取所有老师信息
    serializer_class = TeacherSerializer  # 使用TeacherSerializer进行序列化


class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all().order_by('-id')
    serializer_class = FeeSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all().order_by('-id')
    serializer_class = PeriodSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('-id')
    serializer_class = LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer


class FeeDetailViewSet(viewsets.ModelViewSet):
    queryset = FeeDetail.objects.all().order_by('-id')
    serializer_class = FeeDetailSerializer


class PaymentRecordViewSet(viewsets.ModelViewSet):
    queryset = PaymentRecord.objects.all().order_by('-id')
    serializer_class = PaymentRecordSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = AttendanceSerializer
