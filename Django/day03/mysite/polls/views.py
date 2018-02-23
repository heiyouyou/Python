# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render,get_object_or_404,get_list_or_404

# Create your views here.

from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Question,Choice
import json

def index(request):
	# return HttpResponse("Hello, world. You're at the polls index.")
	# 按照发布日期（pub_date）降序（-）查询前五的问题条目
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	latest_question_list = Question.objects.order_by('-pub_date')
	# output = ','.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
	# 获取视图模板对象，默认是去templates文件夹中查找
	template = loader.get_template('polls/index.html')
	# 定义上下文环境的数据源
	context = {
		'latest_question_list':latest_question_list,
		'message':'这是一个主页的数据源'
	}

	# 返回视图和数据给客户端
	# return HttpResponse(template.render(context,request))
	# 可以使用以下代码替代上面的返回
	return render(request,'polls/index.html',context=context)

class IndexView(generic.ListView):
	# 默认template_name 是应用名/模型名_文件名,需要改变则要进行重写
	template_name = 'polls/index.html'
	# 默认是question_list，改变上下文环境数据中的数据List字段
	context_object_name = 'latest_question_list'

	# 必须重写查询方法
	def get_queryset(self):
		# return Question.objects.order_by('-pub_date')[:5]
		# return Question.objects.order_by('-pub_date')
		# 查询发布日期小于或者等于当前日期的数据
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

	# 需要携带更多其他参数，如下进行设置
	def get_context_data(self,**kwargs):
		context = super(IndexView,self).get_context_data(**kwargs)
		context['now'] = timezone.now()	
		context['message'] = '这是一个主页的数据源'
		# print context
		return context	

def test(request):
	# return HttpResponse("Hello, world. You're at the polls test.",content_type='text/plain')
	response = HttpResponse()
	# 以字典的形式，自定义为response对象扩展属性
	response['Age'] = 25
	response['Name'] = 'youyou'
	# 删除属性
	del response['Name']

	# 将响应头对象当作文件读写对象(file-like-object)返回，注意一定要用return语句返回
	response.write("<p>Here's the text of the Web page.</p>")
	response.write("<p>Here's another paragraph.</p>")
	return response

def test2(request):
	data = {
		"name":"test2"
	}
	return render(request,'polls/test2.html',context=data,content_type='text/plain')

def latest(request):
    return HttpResponse("You're looking at latest.html")

def detail(request,question_id):
	# 重写捕获异常返回的信息
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	# # return HttpResponse("You're looking at question %s." % question_id)

	# 可以使用get_object_or_404或者get_list_or_404替代上面的异常捕获
	# 1:
	# queryset = Question.objects.filter(question_text__startswith='W') #返回一个Queryset实例，并不是List实例
	# print queryset,type(queryset)
	# question = get_object_or_404(queryset,pk=question_id)
	# 2:
	question = get_object_or_404(Question,pk=question_id)
	# 3:
	# question = get_object_or_404(Question,question_text__startswith='W',pk=question_id)
	# 4:
	# question = get_list_or_404(Question,pk=question_id)#get_list_or_404()返回的是一个List实例

	return render(request,'polls/details.html',context={"question":question})

class DetailView(generic.DetailView):
	# 需要使用model属性指定视图类作用于哪个模型
	model = Question
	template_name = 'polls/details.html'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())





def results(request,question_id):
	# question = Question.objects.get(pk=question_id)
	# response = "You're looking at the results of question %s(%s)."
	# return HttpResponse(response % (question_id,question.question_text))

	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{"question":question})

# 访问某个具体数据时，它是通过pk字段进行访问查询的，所以urls.py中的question_id需要改成pk
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		print request.POST['choice']
		# 查询指定id的choice与当前question对象相关的choice对象
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):#
		return render(request,'polls/details.html',{
				'question':question,
				'error_message':"You didn't select a choice!",
			})
	else:
		# 更新choice对象并保存到数据库中
		selected_choice.votes +=1
		selected_choice.save()
		# 页面重定向到results页面，使用reverse函数将url和参数结合起来返回一个string
		# return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
		# 或者：
		return HttpResponseRedirect(reverse('polls:results',kwargs={'pk':question_id},current_app='polls'))
    	# return HttpResponse("You're voting on question %s." % question_id)

def ajax_html(request):
	return render(request,'polls/ajax.html')

def ajax_data(request):
	print request.method
	if  request.method.lower() == 'post':
		user = request.POST['user']
		pwd = request.POST['pwd']
		print user,pwd
		rdata = {"msg":"this is a success info...好","code":200}
		# 注意一定要序列化处理成字符串，才可以不同语言之间传递数据
		# return HttpResponse(json.dumps(rdata),content_type='text/javascript')

		# response = HttpResponse()
		# response['content_type'] = 'application/json'
		# response.write(json.dumps(rdata))
		# return response

		# 更完善的方法 
		return JsonResponse(rdata)
	else:
		return HttpResponse(json.dumps({"msg":"error...","code":400}))