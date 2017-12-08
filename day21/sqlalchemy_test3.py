# !/usr/bin/env python
# coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship,sessionmaker,subqueryload,joinedload
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine


Base = declarative_base()

class Address(Base):
	"""电子邮件表"""
	__tablename__='addresses'
	id = Column(Integer,primary_key=True)
	email_address = Column(String(30),nullable=False)
	user_id = Column(Integer,ForeignKey('users.id'))
	# 该字段并不是被创建在表中，属于List结构
	user = relationship('User',back_populates='addresses')

	# 格式化控制台打印对象时的格式，与__str__类似
	def __repr__(self):
		return "<Address(email_address='{}')>".format(self.email_address)

class User(Base):
	"""用户表"""
	__tablename__='users'
	# 默认自增键
	id = Column(Integer,primary_key=True)
	name = Column(String(10))
	fullname = Column(String(20))
	password = Column(String(20))
	addresses = relationship('Address',order_by=Address.id,back_populates='user')
	def __repr__(self):
		return "<User(name='%s',fullname='%s',password='%s')>" %(self.name,self.fullname,self.password)

# echo=True是开启调试，这样当我们执行文件的时候会提示相应的文字
engine = create_engine('mysql://root:youyouhei@localhost:3306/test',echo=True)
# 如果表不存在，则自动进行创建并连接数据库，否则只是创建连接
Base.metadata.create_all(engine)
# 创建一个操作数据库的session对像
Session = sessionmaker(bind=engine)
session = Session()

# 添加一条数据
# ed_user = User(name='ed',fullname='Ed Jones',password='edspassword')
# session.add(ed_user)

# # 同时添加多条数据
# session.add_all([
# 	User(name='wendy', fullname='Wendy Williams', password='foobar'),
#     User(name='mary', fullname='Mary Contrary', password='xxg527'),
#     User(name='fred', fullname='Fred Flinstone', password='blah')])

# 查询出所有数据
# users = session.query(User).order_by(User.id)
# print '-----------'
# print users #打印的是一条查询语句对象
# for u in users:
# 	# u为User类的实例
# 	print u 
# 	print u.name,u.fullname

# # 使用filter_by过滤查询
# filter_users = session.query(User.name).filter_by(fullname='Ed Jones')
# print '-----------'
# print filter_users
# for u in filter_users:
# 	print u.name

# 删除
# session.delete(ed_user)
# print session.query(User).filter_by(name='ed').count()


# jack = User(name='jack',fullname='Jack Bean',password='gjffdd')
# # 为对象添加邮箱，将同步为Address表添加数据
# jack.addresses = [Address(email_address='jack@google.com'),Address(email_address='j25@yahoo.com')]
# session.add(jack)

jack = session.query(User).filter_by(name='jack').one()
print jack
print '--------'
# 只有在调用jack.addresses时才会调用查询邮件地址的SQL，这个是典型的懒加载模式
print jack.addresses

# join查询(内联查询)，注意filter()中的等值使用的是双等号，而filter_by使用的是单个等号
jacks = session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()
print jacks

# 不想使用懒加载，而是要强制一次性加载某个关联数据，那么可以使用subqueryload或者joinedload
jackss = session.query(User).options(subqueryload(User.addresses)).filter_by(name='jack').one()
print jackss
print '=============='
# 推荐使用这种方式将关联数据查询出来
jacksss = session.query(User).options(joinedload(User.addresses)).filter_by(name='jack').one()
print jacksss

# 提交事务
session.commit()
# 关闭会话
session.close()