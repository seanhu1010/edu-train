from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from datetime import timedelta
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


# 上课时间
class Period(models.Model):
    start_date = models.DateField(verbose_name="上课日期")
    start_time = models.TimeField(verbose_name="上课开始时间")
    end_time = models.TimeField(verbose_name="上课结束时间")

    def __str__(self):
        return f"{self.start_date} {self.start_time}-{self.end_time}"


# 课模型
class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="关联课程")
    name = models.CharField(max_length=100, verbose_name="课名称")
    subject = models.CharField(max_length=100, blank=True, null=True, verbose_name="所属科目")
    icon = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True, verbose_name="课图标")
    is_active = models.BooleanField(default=True, verbose_name="是否开课")
    mode = models.CharField(max_length=100, default='班级教学',
                            choices=[('班级教学', '班级教学'), ('一对一', '一对一')], verbose_name="上课模式")
    require_leave = models.BooleanField(default=True, verbose_name="学员未到是否要求家长请假")
    leave_limit = models.CharField(max_length=100, default='不限次数',
                                   choices=[('不限次数', '不限次数'), ('不可顺延', '不可顺延')] + [(str(i), str(i)) for
                                                                                                   i in range(31)],
                                   verbose_name="请假次数限制")
    full_class = models.IntegerField(default=10, verbose_name="满班人数")
    class_times = models.IntegerField(default=1, verbose_name="上课次数")
    frequency = models.IntegerField(default=1, verbose_name="上课频率(次/周)")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name="上课时间")


# 课程模型
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="课程名称")
    age_start = models.IntegerField(default=6, verbose_name="适龄年龄起")
    age_end = models.IntegerField(default=18, verbose_name="适龄年龄止")
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name="课程类型")
    times = models.IntegerField(default=1, verbose_name="上课次数")  # 只读，自动计算
    period_num = models.IntegerField(default=10, verbose_name="课程课时数")
    start_time = models.DateTimeField(verbose_name="课程开始时间")
    end_time = models.DateTimeField(verbose_name="课程结束时间")
    location = models.CharField(max_length=100, verbose_name="上课场地")
    is_open = models.BooleanField(default=True, verbose_name="是否开放给家长和老师")
    main_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="主课老师",
                                     related_name='main_courses')
    assistant_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True,
                                          verbose_name="助教老师",
                                          related_name='assistant_courses')
    alternative_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True,
                                            verbose_name="备选老师",
                                            related_name='alternative_courses')
    full_class = models.IntegerField(default=10, verbose_name="满班人数")
    fee_standard = models.ForeignKey(Fee, on_delete=models.CASCADE, verbose_name="收费标准")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程原价")  # 自动计算


# 学员选课关系模型
class FeeDetail(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="学员")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    buy_period = models.IntegerField(verbose_name="购买课时数")
    gift_period = models.IntegerField(default=0, verbose_name="赠送课时数")
    total_period = models.IntegerField(verbose_name="总课时")  # 自动计算
    remaining_period = models.IntegerField(verbose_name="剩余课时数")  # 自动赋值
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="优惠减免")
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="优惠后价格")  # 自动计算
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="实缴学费")  # 自动更新
    unpaid_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="欠缴学费")  # 自动更新
    salesperson = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="销售人")
    remind_renewal = models.BooleanField(default=True, verbose_name="续费提醒")
    renewal_fee_standard = models.ForeignKey(Fee, on_delete=models.CASCADE, verbose_name="续费价格标准")
    remark = models.TextField(blank=True, null=True, verbose_name="备注")
    contract_pic = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True, verbose_name="合同图")
    valid_until = models.DateTimeField(verbose_name="有效期至")  # 自动赋值


# 缴费记录表
class PaymentRecord(models.Model):
    fee_detail = models.ForeignKey(FeeDetail, on_delete=models.CASCADE, verbose_name="费用详情")
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="缴纳费用")
    payment_method = models.CharField(max_length=100, default='微信', verbose_name="支付方式")
    payer = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="缴费人")
    payment_time = models.DateTimeField(default=timezone.now, verbose_name="缴费时间")
    fee_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name="费用标签")
    remark = models.TextField(blank=True, null=True, verbose_name="备注")


# 签到记录模型
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="学员")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="课")
    status = models.CharField(max_length=100, default='未处理',
                              choices=[('出勤', '出勤'), ('请假', '请假'), ('旷课', '旷课'), ('未处理', '未处理')],
                              verbose_name="考勤状态")
    is_active = models.BooleanField(default=True, verbose_name="失效状态")


# 信号处理函数
@receiver(post_save, sender=Lesson)
def update_course_times(sender, instance, **kwargs):
    # 当课程Lesson保存后，自动更新关联的课程Course的上课次数
    course = instance.course
    course.times = Lesson.objects.filter(course=course).count()
    course.save(update_fields=['times'])


@receiver(pre_save, sender=Course)
def update_course_original_price(sender, instance, **kwargs):
    # 当课程Course保存前，自动更新课程的原价
    course = instance
    course.original_price = course.period_num * course.fee_standard.fee_price


@receiver(pre_save, sender=FeeDetail)
def update_fee_detail_fields(sender, instance, **kwargs):
    # 在费用详情FeeDetail保存前，自动计算并更新总课时、剩余课时、优惠后价格和有效期至等字段
    fee_detail = instance
    fee_detail.total_period = fee_detail.course.period_num + fee_detail.gift_period
    fee_detail.remaining_period = fee_detail.total_period
    fee_detail.discounted_price = fee_detail.course.original_price - fee_detail.discount
    fee_detail.unpaid_fee = fee_detail.discounted_price - fee_detail.paid_fee
    fee_detail.valid_until = fee_detail.course.end_time + timedelta(days=180)


@receiver(post_save, sender=PaymentRecord)
def update_fee_detail_paid_fee(sender, instance, **kwargs):
    # 当缴费记录PaymentRecord保存后，自动更新关联的费用详情FeeDetail的实缴学费和欠缴学费
    payment_record = instance
    fee_detail = payment_record.fee_detail
    fee_detail.paid_fee = PaymentRecord.objects.filter(fee_detail=fee_detail).aggregate(Sum('paid_fee'))[
        'paid_fee__sum']
    fee_detail.unpaid_fee = fee_detail.discounted_price - fee_detail.paid_fee
    fee_detail.save(update_fields=['paid_fee', 'unpaid_fee'])


@receiver(post_save, sender=FeeDetail)
def create_attendance_records(sender, instance, created, **kwargs):
    # 当费用详情FeeDetail创建后，自动创建关联的学员和课程的签到记录Attendance
    if created:
        fee_detail = instance
        student = fee_detail.student
        lessons = Lesson.objects.filter(course=fee_detail.course)
        for lesson in lessons:
            Attendance.objects.create(student=student, lesson=lesson)
