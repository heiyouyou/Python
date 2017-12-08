# !/usr/bin/ env python
# coding=utf-8

# 导入MySQL-python驱动
import MySQLdb

# 连接MySQL数据库，输入连接地址、指定用户和口令以及访问的数据库与mysol.connector的参数设置有些不同
conn = MySQLdb.connect('localhost','root','youyouhei','test')
# 创建操作数据库的交互对象
cursor = conn.cursor()
# 创建表
cursor.execute('CREATE TABLE IF NOT EXISTS user (id varchar(20) primary key,name varchar(20))')
try:
	# 删除数据
	cursor.execute('DELETE FROM user')
	# 插入数据
	cursor.execute('INSERT INTO users VALUES (%s,%s)',['1','wzy'])
	cursor.execute('INSERT INTO user VALUES (%s,%s)',['2','heiyouyou'])
	print cursor.rowcount
	print 'insert successfully....'
	conn.commit()
except:
	# 发生错误时回滚
	print 'error...'
   	conn.rollback()
finally:
	cursor.close()
	# 如果Cursor对象关闭，要重新创建，否则报错
	cursor = conn.cursor()
	# 查询数据
	# 占位符对应的数据可以使用元组或者列表填充
	# cursor.execute('SELECT * FROM user  WHERE id=%s',['1'])
	# cursor.execute('SELECT * FROM user  WHERE id=%s',('1',])
	cursor.execute('SELECT * FROM user')
	# cursor.fetchone() #获取单条数据，返回的是一个元组元素
	values = cursor.fetchall() #获取所有符合条件的数据，返回的是一个二维元组
	print values
	for v in values:
		print v[0],'----',v[1]
	print 'select successfully....'
	cursor.close()
	conn.close()
	