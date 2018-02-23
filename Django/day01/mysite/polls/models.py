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
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

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