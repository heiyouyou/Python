# !/usr/bin/env python
# coding=utf-8

# 导入SQLite驱动
import os,sqlite3

# 判断是否存在test.db文件，如果存在则进行删除，不然创建表会报重创建的错误
db_file = os.path.join(os.path.dirname('.'),'test.db')
if os.path.exists(db_file):
	os.remove(db_file)

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect(db_file)
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('CREATE TABLE user (id varchar(20) primary key,name varchar(20))')
# 执行插入语句
cursor.execute(r'insert INTO user (id,name) values("1","wzy")')
cursor.execute(r'insert INTO user (id,name) values("2","youyou")')
cursor.execute(r'insert INTO user (id,name) values("3","heiyouyou")')
# 通过rowcount获得插入的行数:
print cursor.rowcount
print '--------'
# 执行查询id为1的语句
cursor.execute('SELECT * FROM user WHERE id=?',('2',))
# 获得查询结果集:
values = cursor.fetchall() 
print values
# 关闭Cursor:
cursor.close()
# 提交事务
conn.commit
# 关闭连接
conn.close()


