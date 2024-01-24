from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


# 字典表模型
class Dictionary(models.Model):
    name = models.CharField(max_length=100, verbose_name="字典名称")
    type = models.CharField(max_length=100, verbose_name="字典类型")
    is_active = models.BooleanField(default=True, verbose_name="失效状态")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者",
                                related_name='created_dictionaries')
    created_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updater = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="更新者",
                                related_name='updated_dictionaries')
    updated_time = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    remark = models.TextField(blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.name


# 字典数据表模型
class DictionaryData(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="字典")
    text = models.CharField(max_length=100, verbose_name="字典项文本")
    value = models.CharField(max_length=100, verbose_name="字典项值")
    order = models.IntegerField(verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="失效状态")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者",
                                related_name='created_dic_datas')
    created_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updater = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="更新者",
                                related_name='updated_dic_datas')
    updated_time = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    remark = models.TextField(blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.text


# 头像表模型
class Avatar(models.Model):
    file = models.ImageField(upload_to='avatars/', verbose_name="头像文件")
    name = models.CharField(max_length=100, blank=True, default=str(uuid.uuid4), verbose_name="头像名称")

    def __str__(self):
        return self.name


# 家长表模型
class Parent(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, verbose_name="家长头像")
    role = models.CharField(max_length=100, verbose_name="家长角色")
    name = models.CharField(max_length=100, verbose_name="家长姓名")
    birthday = models.DateField(blank=True, null=True, verbose_name="家长生日")
    address = models.TextField(blank=True, null=True, verbose_name="家庭住址")
    is_active = models.BooleanField(default=True, verbose_name="激活状态")
    phone = models.CharField(max_length=20, verbose_name="家长电话")
    wechat = models.CharField(max_length=100, blank=True, null=True, verbose_name="家长微信号")

    def __str__(self):
        return self.name


# 流失表模型
class Dropout(models.Model):
    description = models.TextField(verbose_name="流失说明")

    def __str__(self):
        return self.description


# 老师信息模型
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    phone = models.CharField(max_length=20, verbose_name="手机号")
    id_card = models.CharField(max_length=50, verbose_name="身份证号")
    level = models.CharField(max_length=100, verbose_name="老师级别")

    def __str__(self):
        return self.name


# 学员信息模型
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name="昵称")
    gender = models.CharField(max_length=10, verbose_name="性别")
    birthday = models.DateField(verbose_name="生日")
    address = models.TextField(verbose_name="家庭住址")
    # parent_name = models.CharField(max_length=100, verbose_name="家长姓名")
    # parent_phone = models.CharField(max_length=20, verbose_name="家长手机号")
    id_type = models.ForeignKey(DictionaryData, on_delete=models.CASCADE, verbose_name="证件类型")
    id_card = models.CharField(max_length=50, verbose_name="证件号码")
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, verbose_name="学员头像")
    dropout = models.ForeignKey(Dropout, on_delete=models.CASCADE, blank=True, null=True, verbose_name="流失id")
    school = models.CharField(max_length=100, blank=True, null=True, verbose_name="学校")
    grade = models.CharField(max_length=100, blank=True, null=True, verbose_name="年级")
    class_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="班级")
    nationality = models.CharField(max_length=100, blank=True, null=True, verbose_name="国籍")
    ethnicity = models.CharField(max_length=100, blank=True, null=True, verbose_name="民族")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者", related_name='created_students')
    created_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updater = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="更新者", related_name='updated_students')
    updated_time = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    remark = models.TextField(blank=True, null=True, verbose_name="备注")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="家长id")
    recruiter = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="招生老师")
    status = models.CharField(max_length=100, default='在读', verbose_name="学员状态")
    is_active = models.BooleanField(default=True, verbose_name="失效状态")
    class_status = models.CharField(max_length=100, default='未分班', verbose_name="分班状态")
    source = models.CharField(max_length=100, default='到访', verbose_name="招生来源")
    tag = models.CharField(max_length=100, blank=True, null=True, verbose_name="学员标签")

    def __str__(self):
        return self.name


# 费用信息模型
class Fee(models.Model):
    fee_type = models.CharField(max_length=100, verbose_name="课时费用类型")
    fee_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课时费用单价")

    def __str__(self):
        return f'{self.fee_type}:{self.fee_price}/课时'


# 星期模型
class LessonTime(models.Model):
    DAY_CHOICES = [
        (1, '周一'),
        (2, '周二'),
        (3, '周三'),
        (4, '周四'),
        (5, '周五'),
        (6, '周六'),
        (7, '周天'),
    ]
    day_of_week = models.IntegerField(choices=DAY_CHOICES, blank=False, verbose_name="上课天")
    lesson_start_time = models.TimeField(verbose_name="上课时间")  # 上课时间
    lesson_end_time = models.TimeField(verbose_name="下课时间")  # 下课时间

    def __str__(self):
        day = self.get_day_of_week_display()  # 模型实例的 get_<field_name>_display() 方法获取可读标签
        return f'{day}{self.lesson_start_time} 至 {day}{self.lesson_end_time}'


# 课程信息模型
class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name="课程名")
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name="授课老师")
    max_students = models.IntegerField(verbose_name="满班人数")
    course_time = models.ManyToManyField(LessonTime, verbose_name="上课时间")
    course_lessons = models.IntegerField(verbose_name="课程课时数")
    course_fee_type = models.ForeignKey(Fee, on_delete=models.CASCADE, verbose_name="课程费用类型")
    start_time = models.DateField(verbose_name="课程开课时间")
    end_time = models.DateField(verbose_name="课程结束时间")

    def __str__(self):
        return self.course_name


# 学员选课关系模型
class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name="学员")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程")
    course_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程费用")
    remaining_lessons = models.IntegerField(verbose_name="剩余课时数")
    bill_status = models.BooleanField(default=False, verbose_name="账单状态")


# 签到记录模型
class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name="学员")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程")
    check_in_time = models.DateTimeField(verbose_name="签到时间")  # 签到时间
    absent = models.BooleanField(default=False, verbose_name="是否缺勤")  # 是否缺勤
