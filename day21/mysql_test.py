# !/usr/bin/ env python
# coding=utf-8

# 导入mysql-connector-python驱动
import mysql.connector

# 连接MySQL数据库，输入指定用户和口令以及访问的数据库
conn = mysql.connector.connect(user='root',password='youyouhei',database='test',use_unicode=True)
cursor = conn.cursor()
# 创建表
cursor.execute('CREATE TABLE IF NOT EXISTS user (id varchar(20) primary key,name varchar(20))')
# 删除数据
cursor.execute('DELETE FROM user')
# 插入数据
cursor.execute('INSERT INTO user VALUES (%s,%s)',['1','Michael'])
cursor.execute('INSERT INTO user VALUES (%s,%s)',['2','youyou'])
print cursor.rowcount
print 'insert successfully....'
conn.commit()
cursor.close()
# 如果Cursor对象关闭，要重新创建，否则报错
cursor = conn.cursor()
# 查询数据
# 占位符对应的数据可以使用元组或者列表填充
# cursor.execute('SELECT * FROM user  WHERE id=%s',['1'])
# cursor.execute('SELECT * FROM user  WHERE id=%s',('1',])
cursor.execute('SELECT * FROM user')
values = cursor.fetchall()
print values
for v in values:
	print v[0],'----',v[1]
print 'select successfully....'
cursor.close()
conn.close()