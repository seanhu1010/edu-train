from rest_framework import serializers
from .models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Student, Teacher, LessonTime, Course, Fee, \
    Enrollment, Attendance


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


# 老师信息序列化器
class LessonTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTime  # 使用LessonTime模型
        fields = '__all__'  # 序列化所有字段


# 课程信息序列化器
class CourseSerializer(serializers.ModelSerializer):
    course_time = LessonTimeSerializer(many=True)  # 将ManyToManyField设置为LessonTimeSerializer的实例

    class Meta:
        model = Course  # 使用Course模型
        fields = '__all__'  # 序列化所有字段


# 费用信息序列化器
class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee  # 使用Fee模型
        fields = '__all__'  # 序列化所有字段


# 学员选课关系序列化器
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment  # 使用Enrollment模型
        fields = '__all__'  # 序列化所有字段


# 签到记录序列化器
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance  # 使用Attendance模型
        fields = '__all__'  # 序列化所有字段
