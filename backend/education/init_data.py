#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:  HUHU
# @File:    init_data.py.py
# @Time:    2024/01/23
"""

"""
import os
import random
import django
import sys
from datetime import datetime, timedelta

sys.path.append('C:/Users/HUHU/PycharmProjects/edu-train/backend')  # 替换为你的项目的根目录的路径

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # 替换为你的settings.py所在的模块
django.setup()

from education.models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, \
    Course, FeeDetail, PaymentRecord, Attendance
from django.contrib.auth.models import User


# 随机生成4位数字，以字符串返回
def generate_random_number():
    number = random.randint(0, 9999)
    return str(number).zfill(4)


# 创建超级用户
def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', '123456')
    print("Superuser created.")


# 创建字典和字典数据
def create_dictionary_and_data(name, data_list):
    admin = User.objects.get(username='admin')
    dictionary, created = Dictionary.objects.get_or_create(name=name, creator=admin, updater=admin)
    for order, data in enumerate(data_list, start=1):
        DictionaryData.objects.get_or_create(dictionary=dictionary, text=data, value=order, order=order, creator=admin,
                                             updater=admin)
    print("Dictionary data created.")


# 创建头像
def create_avatars():
    for filename in os.listdir('../media/avatars'):  # 注意这里的路径已经修改
        if filename.endswith('.jpg'):
            Avatar.objects.get_or_create(file=f'images/{filename}', name=filename[:-4])
    print("Avatar data created.")


# 创建家长
def create_parents(student_name):
    roles = DictionaryData.objects.filter(dictionary__name='家长角色')
    role = random.choice(roles)
    avatars = Avatar.objects.all()
    parent, created = Parent.objects.get_or_create(avatar=random.choice(avatars), role=role,
                                                   name=f'{student_name}{role}',
                                                   phone=f'1380013{generate_random_number()}')
    return parent


# 创建流失
def create_dropout():
    for i in range(3):
        Dropout.objects.get_or_create(description=f'流失原因{i}')
    print("Dropout data created.")


# 创建老师
def create_teachers():
    for i in range(3):
        Teacher.objects.get_or_create(name=f'老师{i}', phone=f'1580013800{i}', level=f'级别{i}')
    print("Teacher data created.")


# 创建学员
def create_students():
    admin = User.objects.get(username='admin')
    genders = DictionaryData.objects.filter(dictionary__name='性别')
    teachers = Teacher.objects.all()
    avatars = Avatar.objects.all()
    id_type = DictionaryData.objects.get(dictionary__name='证件类型', text='身份证')
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2018, 12, 31)
    time_between_dates = end_date - start_date
    for teacher in teachers:
        for i in range(random.randint(1, 20)):
            n4 = generate_random_number()
            name = f'学员{n4}'
            if not Student.objects.filter(name=name).exists():
                parent = create_parents(name)
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                birthday = start_date + timedelta(days=random_number_of_days)
                Student.objects.get_or_create(avatar=random.choice(avatars), gender=random.choice(genders),
                                              recruiter=teacher, parent=parent,
                                              name=name, id_card=f'11010120010{n4}', id_type=id_type, birthday=birthday,
                                              creator=admin, updater=admin)
    print("Student data created.")


# 创建费用
def create_fees():
    for i in range(1, 3):
        Fee.objects.get_or_create(fee_type=f'类型{i}', fee_price=f'{i}00.00')
    print("Fee data created.")


# 创建课程
def create_courses():
    teachers = Teacher.objects.all()
    fees = Fee.objects.all()
    for i in range(3):
        if not Course.objects.filter(name=f'课程{i}').exists():
            Course.objects.get_or_create(name=f'课程{i}', start_time='2024-01-01', end_time='2024-12-31',
                                         location=f'场地{i}', main_teacher=random.choice(teachers),
                                         fee_standard=random.choice(fees))
    print("Course data created.")


# 创建课时和课
def create_periods_and_lessons():
    start_dates = ['2024-01-22 08:30:00', '2024-01-22 10:20:00', '2024-01-22 13:30:00']
    courses = Course.objects.all()

    for i, course in enumerate(courses):
        start_date = datetime.strptime(start_dates[i % 3], '%Y-%m-%d %H:%M:%S')
        for j in range(12):
            while start_date.weekday() > 4:  # 如果是周六或周日，则跳到下一天
                start_date += timedelta(days=1)
            end_date = start_date + timedelta(hours=1, minutes=30)
            period = Period.objects.create(start_date=start_date.date(), start_time=start_date.time(),
                                           end_time=end_date.time())
            Lesson.objects.create(name=f'{course.name}的第{j + 1}课',
                                  course=course, period=period)
            start_date += timedelta(days=1)
    print("Period and Lesson data created.")


# 对每个学生随机选择一门课程，生成对应的费用详情，并生成缴费记录
def create_fee_detail():
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    for student in students:
        # 检查学生是否已经选修过课程或剩余课时为0
        enrollments = FeeDetail.objects.filter(student=student)
        if not enrollments.exists() or all(enrollment.remaining_period == 0 for enrollment in enrollments):
            course = random.choice(courses)
            FeeDetail.objects.create(student=student, course=course, buy_period=course.period_num,
                                     salesperson=random.choice(teachers),
                                     renewal_fee_standard=course.fee_standard)
        # 创建缴费记录
        fee_details = FeeDetail.objects.filter(student=student)
        for fee_detail in fee_details:
            if fee_detail.unpaid_fee > 0:
                paid_fee = 1000
                PaymentRecord.objects.create(fee_detail=fee_detail, paid_fee=paid_fee, payer=student.parent)
    print("FeeDetail data created.")


# 初始化数据
def init_data():
    create_superuser()
    create_dictionary_and_data('性别', ['男', '女'])
    create_dictionary_and_data('证件类型', ['身份证', '港澳通行证', '台湾通行证', '护照'])
    create_dictionary_and_data('家长角色',
                               ['妈妈', '爸爸', '爷爷', '奶奶', '外公', '外婆', '哥哥', '姐姐', '自己', '叔叔', '阿姨',
                                '伯父', '伯母', '舅舅', '舅妈', '姨父', '姨妈', '姑父', '姑姑', '弟弟', '妹妹', '干爸',
                                '干妈'])
    create_dictionary_and_data('学员状态', ['待跟进', '在读', '流失'])
    create_dictionary_and_data('失效状态', ['有效', '失效'])
    create_dictionary_and_data('分班状态', ['已分班', '未分班'])
    create_dictionary_and_data('招生来源', ['到访', '地推', '转介绍', '分享推广', '其他'])
    create_dictionary_and_data('学员标签', ['重点'])
    create_dictionary_and_data('国家',
                               ['安道尔', '阿联酋', '阿富汗', '安提瓜和巴布达', '安圭拉', '阿尔巴尼亚', '亚美尼亚',
                                '安哥拉', '南极洲', '阿根廷', '美属萨摩亚', '奥地利', '澳大利亚', '阿鲁巴', '奥兰群岛',
                                '阿塞拜疆', '波黑', '巴巴多斯', '孟加拉', '比利时', '布基纳法索', '保加利亚', '巴林',
                                '布隆迪', '贝宁', '圣巴泰勒米岛', '百慕大', '文莱', '玻利维亚', '荷兰加勒比区', '巴西',
                                '巴哈马', '不丹', '布韦岛', '博茨瓦纳', '白俄罗斯', '伯利兹', '加拿大', '科科斯群岛',
                                '中非', '瑞士', '智利', '喀麦隆', '哥伦比亚', '哥斯达黎加', '古巴', '佛得角', '圣诞岛',
                                '塞浦路斯', '捷克', '德国', '吉布提', '丹麦', '多米尼克', '多米尼加', '阿尔及利亚',
                                '厄瓜多尔', '爱沙尼亚', '埃及', '西撒哈拉', '厄立特里亚', '西班牙', '芬兰', '斐济群岛',
                                '马尔维纳斯群岛', '密克罗尼西亚联邦', '法罗群岛', '法国', '加蓬', '格林纳达',
                                '格鲁吉亚', '法属圭亚那', '加纳', '直布罗陀', '格陵兰', '几内亚', '瓜德罗普',
                                '赤道几内亚', '希腊', '南乔治亚岛和南桑威奇群岛', '危地马拉', '关岛', '几内亚比绍',
                                '圭亚那', '赫德岛和麦克唐纳群岛', '洪都拉斯', '克罗地亚', '海地', '匈牙利', '印尼',
                                '爱尔兰', '以色列', '马恩岛', '印度', '英属印度洋领地', '伊拉克', '伊朗', '冰岛',
                                '意大利', '泽西岛', '牙买加', '约旦', '日本', '柬埔寨', '基里巴斯', '科摩罗', '科威特',
                                '开曼群岛', '黎巴嫩', '列支敦士登', '斯里兰卡', '利比里亚', '莱索托', '立陶宛',
                                '卢森堡', '拉脱维亚', '利比亚', '摩洛哥', '摩纳哥', '摩尔多瓦', '黑山', '法属圣马丁',
                                '马达加斯加', '马绍尔群岛', '马其顿', '马里', '缅甸', '马提尼克', '毛里塔尼亚',
                                '蒙塞拉特岛', '马耳他', '马尔代夫', '马拉维', '墨西哥', '马来西亚', '纳米比亚',
                                '尼日尔', '诺福克岛', '尼日利亚', '尼加拉瓜', '荷兰', '挪威', '尼泊尔', '瑙鲁', '阿曼',
                                '巴拿马', '秘鲁', '法属波利尼西亚', '巴布亚新几内亚', '菲律宾', '巴基斯坦', '波兰',
                                '皮特凯恩群岛', '波多黎各', '巴勒斯坦', '帕劳', '巴拉圭', '卡塔尔', '留尼汪',
                                '罗马尼亚', '塞尔维亚', '俄罗斯', '卢旺达', '所罗门群岛', '塞舌尔', '苏丹', '瑞典',
                                '新加坡', '斯洛文尼亚', '斯瓦尔巴群岛和扬马延岛', '斯洛伐克', '塞拉利昂', '圣马力诺',
                                '塞内加尔', '索马里', '苏里南', '南苏丹', '圣多美和普林西比', '萨尔瓦多', '叙利亚',
                                '斯威士兰', '特克斯和凯科斯群岛', '乍得', '多哥', '泰国', '托克劳', '东帝汶', '突尼斯',
                                '汤加', '土耳其', '图瓦卢', '坦桑尼亚', '乌克兰', '乌干达', '美国', '乌拉圭', '梵蒂冈',
                                '委内瑞拉', '英属维尔京群岛', '美属维尔京群岛', '越南', '瓦利斯和富图纳', '萨摩亚',
                                '也门', '马约特', '南非', '赞比亚', '津巴布韦', '中国', '刚果布', '刚果金', '莫桑比克',
                                '根西岛', '冈比亚', '北马里亚纳群岛', '埃塞俄比亚', '新喀里多尼亚', '瓦努阿图',
                                '法属南部领地', '纽埃', '美国本土外小岛屿', '库克群岛', '英国', '特立尼达和多巴哥',
                                '圣文森特和格林纳丁斯', '新西兰', '沙特阿拉伯', '老挝', '朝鲜北朝鲜', '韩国南朝鲜',
                                '葡萄牙', '吉尔吉斯斯坦', '哈萨克斯坦', '塔吉克斯坦', '土库曼斯坦', '乌兹别克斯坦',
                                '圣基茨和尼维斯', '圣皮埃尔和密克隆', '圣赫勒拿', '圣卢西亚', '毛里求斯', '科特迪瓦',
                                '肯尼亚', '蒙古国'])
    create_dictionary_and_data('民族',
                               ['壮族', '藏族', '裕固族', '彝族', '瑶族', '锡伯族', '乌孜别克族', '维吾尔族', '佤族',
                                '土家族', '土族', '塔塔尔族', '塔吉克族', '水族', '畲族', '撒拉族', '羌族', '普米族',
                                '怒族', '纳西族', '仫佬族', '苗族', '蒙古族', '门巴族', '毛南族', '满族', '珞巴族',
                                '僳僳族', '黎族', '拉祜族', '柯尔克孜族', '景颇族', '京族', '基诺族', '回族', '赫哲族',
                                '哈萨克族', '哈尼族', '仡佬族', '高山族', '鄂温克族', '俄罗斯族', '鄂伦春族', '独龙族',
                                '东乡族', '侗族', '德昂族', '傣族', '达斡尔族', '朝鲜族', '布依族', '布朗族', '保安族',
                                '白族', '阿昌族', '汉族'])
    create_avatars()
    create_dropout()
    create_teachers()
    create_students()
    create_fees()
    create_courses()
    create_periods_and_lessons()
    create_fee_detail()


if __name__ == '__main__':
    init_data()
