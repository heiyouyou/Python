# !/usr/bin/env python
# coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

# 格式化一个邮件地址
def _fromat_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8') if isinstance(addr,unicode) else addr))
	# 经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本。
from_addr = raw_input('From: ')
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ')
to_addr = raw_input('To: ')

msg = MIMEText('hello,send by Python...','plain','utf-8')
msg['From'] = _fromat_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _fromat_addr(u'管理员 <%s>' % to_addr) #接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可
msg['Subject'] = Header(u'来自SMTP的问候...','utf-8').encode()
# print msg

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addrs], msg.as_string())
server.quit()
