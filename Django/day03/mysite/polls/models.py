# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


	# 不支持中文
	# def __str__(self):
	# 	return self.question_text
	# 支持中文
	def __unicode__(self):
		return self.question_text
	def was_published_recently(self):
		# return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
		return timezone.now()-datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

	# 通过以下几个属性对 对象的方法进行属性的升降序设置，按照发布日期排序
	was_published_recently.admin_order_field = 'pub_date'
	# 控制显示图标还是文字
	was_published_recently.boolean = True
	# 表头的标题
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text
class Test(models.Model):
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name