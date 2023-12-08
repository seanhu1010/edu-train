from django.db import models


# 学员信息模型
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name="昵称")
    gender = models.CharField(max_length=10, verbose_name="性别")
    birthday = models.DateField(verbose_name="生日")
    address = models.TextField(verbose_name="家庭住址")
    parent_name = models.CharField(max_length=100, verbose_name="家长姓名")
    parent_phone = models.CharField(max_length=20, verbose_name="家长手机号")
    id_card = models.CharField(max_length=50, verbose_name="学员身份证号")

    def __str__(self):
        return self.name


# 老师信息模型
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    phone = models.CharField(max_length=20, verbose_name="手机号")
    id_card = models.CharField(max_length=50, verbose_name="身份证号")
    level = models.CharField(max_length=100, verbose_name="老师级别")

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
