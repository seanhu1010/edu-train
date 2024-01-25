from rest_framework import viewsets
from .models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, Course, \
    FeeDetail, PaymentRecord, Attendance
from .serializers import DictionarySerializer, DictionaryDataSerializer, AvatarSerializer, ParentSerializer, \
    DropoutSerializer, TeacherSerializer, StudentSerializer, FeeSerializer, PeriodSerializer, LessonSerializer, \
    CourseSerializer, FeeDetailSerializer, PaymentRecordSerializer, AttendanceSerializer


# 字典表视图
class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


# 字典数据表视图
class DictionaryDataViewSet(viewsets.ModelViewSet):
    queryset = DictionaryData.objects.all()
    serializer_class = DictionaryDataSerializer


# 头像表视图
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


# 家长表视图
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


# 流失表视图
class DropoutViewSet(viewsets.ModelViewSet):
    queryset = Dropout.objects.all()
    serializer_class = DropoutSerializer


# 学员信息视图
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  # 从数据库中获取所有学员信息
    serializer_class = StudentSerializer  # 使用StudentSerializer进行序列化


# 老师信息视图
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()  # 从数据库中获取所有老师信息
    serializer_class = TeacherSerializer  # 使用TeacherSerializer进行序列化


class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class FeeDetailViewSet(viewsets.ModelViewSet):
    queryset = FeeDetail.objects.all()
    serializer_class = FeeDetailSerializer


class PaymentRecordViewSet(viewsets.ModelViewSet):
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentRecordSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
