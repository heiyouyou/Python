# coding=utf-8
from django.shortcuts import render
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
from django.template import loader
from datetime import datetime

from .models import Reporter,Article

# Create your views here.


@require_http_methods(["GET","POST"])
def test(request):
	return render(request,'testdb/test.html',context={"data":'this is get test html...'})

@require_GET
def data(request):
	# select_template与get_template效果类似，都会返回一个Template对象，只是接受的第一个参数不一样
	# 前者使用List列表接受多个template，template engine 查找template直到存在为止就不会继续查找
	template = loader.select_template(['testdb/data_test.html','testdb/datas.html','testdb/data2.html','testdb/data.html'])
	context = {
		"data2":"this is select_template...",
		"data":"this is get test html...",
		"data_test":"this is data_test html...",
		"my_date":datetime.now(),
		"list":[1,2,3],
		"filesize":123223234,
		"athlete_list":[
			{
				'name':'Micale Jordan',
				'age':60,
				'job':'basketball'
			},
			{
				'name':'LiLi',
				'age':30,
				'job':'volleball'
			},
			{
				'name':'Norda ell',
				'age':30,
				'job':'tennis'
			}
		],
	}
	return HttpResponse(template.render(context,request))
	# return render(request,'testdb/data.html',context={"data":'this is get test html...'})

@require_POST
def post_data(request):
	return HttpResponse('this is post request data...')

@require_GET
def get_data(request):
	return HttpResponse('this is get request data...')

@require_GET
def test_base(request):
	r = Reporter.objects.get(pk=1)
	data = {
		"name":"youyou",
		"not_name":"<script>alert('hello')</script>",
		"not_name2":"<b>粗体</b>",
		"r1":r
	}
	return render(request,'testdb/test_base.html',context=data)

@require_GET
def test2(request):
	return render(request,'testdb/test2.html')

@require_GET
def router(request):
	return render(request,'testdb/router.html')