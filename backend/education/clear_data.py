#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:  HUHU
# @File:    init_data.py.py
# @Time:    2024/01/23
"""

"""
import os
import django
import sys

sys.path.append('C:/Users/HUHU/PycharmProjects/edu-train/backend')  # 替换为你的项目的根目录的路径

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # 替换为你的settings.py所在的模块
django.setup()

from education.models import Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, \
    Course, FeeDetail, PaymentRecord, Attendance


# 清除数据
def clear_data():
    models = [Dictionary, DictionaryData, Avatar, Parent, Dropout, Teacher, Student, Fee, Period, Lesson, Course, \
              FeeDetail, PaymentRecord, Attendance]
    for model in models:
        model.objects.all().delete()
    print("Data cleared.")


if __name__ == '__main__':
    clear_data()
