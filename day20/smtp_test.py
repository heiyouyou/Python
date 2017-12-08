# !/usr/bin/env python
# coding=utf-8

from email.mime.text import MIMEText

msg = MIMEText('hello,send by Python...','plain','utf-8')
from_addr = raw_input('From: ')
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ')
to_addr = raw_input('To: ')

import smtplib
# 创建SMTP协议对象，默认端口是25
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1) #打印出和SMTP服务器交互的所有信息
server.login(from_addr,password) #登录SMTP服务器
server.sendmail(from_addr,[to_addr],msg.as_string()) #发送邮件，可以是多个收件人list格式，邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()#退出