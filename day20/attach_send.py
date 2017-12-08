# !/usr/bin/env python
# coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

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

# 创建邮件对象
msg = MIMEMultipart()
# 发送人、接受人、主题格式化
msg['From'] = _fromat_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _fromat_addr(u'管理员 <%s>' % to_addr) #接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可
msg['Subject'] = Header(u'来自SMTP的问候...','utf-8').encode()
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...','plain','utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.png','rb') as f:
	mime = MIMEBase('image','png',filename='test.png')
	# 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addrs], msg.as_string())
server.quit()
