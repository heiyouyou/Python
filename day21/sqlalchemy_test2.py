# !/usr/bin/env python
# coding=utf-8
# 导入相关驱动
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey


# 创建对象的基类
Base = declarative_base()

# 创建User对象
class User(Base):
	__tablename__ = 'user'
	# 表结构
	id = Column(String(20),primary_key=True)
	name = Column(String(20))
	books = relationship('Book')
# 创建Book对象
class Book(Base):
	__tablename__ = 'book'
	id = Column(String(20),primary_key=True)
	name = Column(String(20))
	# 建立外键约束
	user_id = Column(String(20),ForeignKey('user.id'))

# 初始化数据库连接
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:youyouhei@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象，Session对象可视为当前数据库连接。
# session = DBSession()
# new_user = User(id='4',name='Mike')
# # 添加记录
# session.add(new_user)
# session.commit()
# # 关闭session
# session.close()
# 添加Book记录


session = DBSession()
new_book1 = Book(id='1',name='HTML5权威指南')
new_book2 = Book(id='2',name='Javascript权威指南')
# 添加多条记录
session.add(new_book1)
session.add(new_book2)
session.commit()
# 关闭session
session.close()


