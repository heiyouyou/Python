# !/usr/bin/env python
# coding=utf-8

import hashlib


def calc_md5(user,password):
	md5 = hashlib.md5()
	md5.update(password+user+'_wzy')
	return md5.hexdigest()
print calc_md5('hei','123456789')
print calc_md5('heiyou','黑黝黝')
print calc_md5('heiyou','heiyouyou')


print '--------------'
db = {}

def register(user,password):
	db[user] = calc_md5(user,password)
	print 'regist %s is successful!' %user

register('michael','123456')
register('bob','abc999')
register('you','123456')
register('alice','alice2008')

def login(user,password):
	md5 = hashlib.md5()
	md5.update(password+user+'_wzy')
	md5_str = md5.hexdigest()
	if user in db and db[user] == md5_str:
		return True
	else:
		return False
	
print login('michael','123456')
print login('bob','abc999')
print login('alice','alice2008')
print login('you','123456')
print '-------------'
print login('michael','1234567')
print login('michaelw','123456')

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文）。
# 只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。