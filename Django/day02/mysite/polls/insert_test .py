# !/usr/bin/env python
# coding=utf-8

import datetime
from django.utils import timezone
from .models import Question,Choice

# 创建对象并且保存到数据库
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30),question_text='where is here?')
future_question.save()
print future_question.was_published_recently()