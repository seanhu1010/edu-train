from rest_framework import serializers
from .models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, Course, \
    FeeDetail, PaymentRecord, Attendance


# 字典表序列化器
class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'


# 字典数据表序列化器
class DictionaryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictionaryData
        fields = '__all__'


# 头像表序列化器
class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'


# 家长表序列化器
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


# 流失表序列化器
class DropoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dropout
        fields = '__all__'


# 学员信息序列化器
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # 使用Student模型
        fields = '__all__'  # 序列化所有字段


# 老师信息序列化器
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher  # 使用Teacher模型
        fields = '__all__'  # 序列化所有字段


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class FeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeDetail
        fields = '__all__'


class PaymentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRecord
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
