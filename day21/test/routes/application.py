# !/usr/bin/env python
# coding=utf-8

import os

__author__ = 'wzy'

def application(environ,start_response):
	method = environ.get('REQUEST_METHOD')
	path = environ.get('PATH_INFO')
	print path
	if 'html' in path:#处理html文件
		start_response('200 OK',[('Content-Type','text/html;charset=UTF-8')])
		jpath = os.path.join(os.getcwd(),os.path.join('views',os.path.split(path)[1]))
		print jpath
		with open(jpath,'r') as f:
			return f.read()
	elif 'css' in path: #处理css文件
		start_response('200 OK',[('Content-Type','text/css')])
		jpath = os.path.join(os.getcwd(),os.path.join('static/css',os.path.split(path)[1]))
		print jpath
		with open(jpath,'r') as f:
			return f.read()
	elif 'js' in path:#处理js文件
		start_response('200 OK',[('Content-Type','application/javascript')])
		jpath = os.path.join(os.getcwd(),os.path.join('static/js',os.path.split(path)[1]))
		print jpath
		with open(jpath,'r') as f:
			return f.read()
	elif 'images' in path:#处理图片
		start_response('200 OK',[('Content-Type','image/jpeg')])
		jpath = os.path.join(os.getcwd(),os.path.join('static/images',os.path.split(path)[1]))
		print jpath
		with open(jpath,'rb') as f:
			return f.read()
	else:
		return '404 Not Found Resources....'
