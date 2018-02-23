# !/usr/bin/env python
# coding=utf-8

from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.core.urlresolvers import reverse


# Create your tests here.

# 测试问题方法的测试用例
class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(),False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(),False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(),True)


def create_question(question_text,days):
	time = timezone.now()+datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text,pub_date=time)


# 测试问题列表主页的用例
class QuestionViewTests(TestCase):
	# 测试没有问题列表的页面状况
	def test_index_view_with_no_quesitons(self):
		# TestCase是实现了Client类的客户端程序
		response = self.client.get(reverse('polls:index'))
		# TestCase内置了一些断言的方法
		self.assertEqual(response.status_code,200)
		self.assertContains(response,'No polls are available.')
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	# 测试包含一个过去问题列表的页面状况
	def test_index_view_with_a_past_quesiton(self):
		create_question(question_text='Past question.',days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])

	# 测试包含一个未来问题列表的页面状况
	def test_index_view_with_a_future_quesiton(self):
		create_question(question_text='Future question.',days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response,"No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	# 测试包含一个未来问题和过去问题列表的页面状况
	def test_index_view_with_future_quesiton_and_past_questions(self):
		create_question(question_text="Past question.",days=-30)
		create_question(question_text="Future question.",days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])
		
	# 测试包含两个过去问题列表的页面状况
	def test_index_view_with_two_past_questions(self):
		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question 2.>', '<Question: Past question 1.>'])


# 测试详情问题页面的用例
class QuestionIndexDetailTests(TestCase):
	def test_detail_view_with_a_future_question(self):
		future_question = create_question(question_text='Future_question.',days=5)
		url = reverse('polls:detail',args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code,404)

	def test_detail_view_with_a_past_question(self):
		past_question = create_question(question_text='Past Question.',days=-5)
		# url = reverse('polls:detail',args=(past_question.id,))
		url = reverse('polls:detail',kwargs={'pk':past_question.id})
		response = self.client.get(url)
		self.assertContains(response,past_question.question_text)

# 测试问题结果列表的用例类
class QuestionIndexResultTests(TestCase):
	def test_result_view_with_a_future_question(self):
		future_question = create_question(question_text='Future_question.',days=5)
		url = reverse('polls:results',args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code,404)

	def test_detail_view_with_a_past_question(self):
		past_question = create_question(question_text='Past Question.',days=-5)
		# url = reverse('polls:results',args=(past_question.id,))
		url = reverse('polls:results',kwargs={'pk':past_question.id})
		response = self.client.get(url)
		self.assertContains(response,past_question.question_text)

