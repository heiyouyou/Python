# !/usr/bin/env python
# coding=utf-8

from wsgiref.simple_server import make_server
from routes.application import application

httpd = make_server('',8000,application)
print 'Serving HTTP on port 8000...'
# 开始监听HTTP请求
httpd.serve_forever()