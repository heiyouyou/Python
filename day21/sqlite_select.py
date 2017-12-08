# !/usr/bin/env python
# coding=utf-8

# 导入SQLite驱动
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个Cursor
cursor = conn.cursor()
# 通过rowcount获得插入的行数:
print cursor.rowcount
print '--------'
# 执行查询id为1的语句
cursor.execute('SELECT * FROM user WHERE id=?',('1',))
# 获得查询结果集:
values = cursor.fetchall() 
print values
# 关闭Cursor:
cursor.close()
# 关闭连接
conn.close()


