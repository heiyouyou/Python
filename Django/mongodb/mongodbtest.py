# -*- coding:utf-8 -*-
# pymongo增删查改

import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient('127.0.0.1',27017)
db = client['test']

tests = db['tests']

data = [
	{
		'title':'今天心情怎么样',
		'content':'心情不是很美丽.....',
		'tag':1,
		'time':datetime.datetime.utcnow()
	},{
		'title':'今天的天气怎么样？',
		'content':'挺冷的.....',
		'tag':2,
		'time':datetime.datetime.utcnow()
	},{
		'title':'你最近过得可好？',
		'content':'嗯.....just so so',
		'tag':2,
		'time':datetime.datetime.utcnow()
	},{
		'title':'再见',
		'content':'再见我最熟悉的陌生人.....',
		'tag':2,
		'time':datetime.datetime.utcnow()
	},
]
# 可以使用save方法插入数据，但是只支持字典形式
# ids = tests.save({
# 	'title':'这是一个测试标题',
# 	'content':'今天的风有点大.....',
# 	'tag':1,
# 	'time':datetime.datetime.utcnow()
# })

# ids = tests.insert_many(data)

# find()返回 Cursor实例
dataList = tests.find({'time':{'$lt':datetime.datetime.utcnow()}})
# print dataList.count()

from bson.objectid import ObjectId

# tests.update({'_id':ObjectId('5a7ac8074c7e362660f880a5')},{'$set':{'title':'今天的风级多大？'}})
# 更新id不存在的数据
# tests.update({'_id':ObjectId('5a7ac8074c7e362660f880a9')},{'$set':{'title':'你什么时候放假？','content':'2月9号放假！','tag':2,'time':datetime.datetime.utcnow()}})#无法更新
# tests.update({'_id':ObjectId('5a7ac8074c7e362660f880a9')},{'$set':{'title':'你什么时候放假？','content':'2月9号放假！','tag':2,'time':datetime.datetime.utcnow()}},True)#不存在就插入一条新数据
# tests.update({'tag':1},{'$set':{'title':'tag为1的更新了。。。'}})#默认多个匹配只更新第一个
# tests.update({'tag':1},{'$set':{'title':'tag为1的全部更新了。。。'}},False)

# 更新多个
# tests.update_many({'tag':1},{'$set':{'title':'tag为1的全部更新了2。。。'}})
# 更新一个
# tests.update_one({'tag':1},{'$set':{'title':'tag为1的只更新了一个。。。'}})

# 删除tag为1的数据，不推荐该方法
# tests.remove({'tag':1})
# 只删除一条匹配的数据
# tests.delete_one({'tag':2})
# 删除所有tag为1的数据
# tests.delete_many({'tag':1})

# print tests.find().count()
# for test in tests.find():
# 	print test

import time
# AND 和 OR 联合使用
# for test in tests.find({'tag':2,'time':{'$lt':datetime.datetime(2018,2,7,16)},'$or':[{'title':'再见','content':'再见我最熟悉的陌生人.....'}]}):
# 	print test,test['time'],(test['time']+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

# $type操作符的使用
# 用途：将tag的值类型为整型（16）integer的文档查询出来
# for test in tests.find({'tag':{'$type':16}},{'title':1,'content':1}):
# 	print test,'\n'


# 指定只能某些键key输出
# 将title、content字段排除查询出所有数据，默认_id是输出（1）
# for test in tests.find({},{'title':0,'content':0}):
# 	print test,'\n'

# 不能将inclusion模式（指定返回的键，不返回其他键）和exclusion模式（指定不返回的键,返回其他键）混合使用，只能全为0或者1
# for test in tests.find({},{'title':1,'content':0}):
# 	print test,'\n'


# sort、limit、skip的使用
for test in tests.find({'time':{'$lte':datetime.datetime(2018,2,7,16)}},{'title':1,'time':1}).limit(2).skip(1).sort([('time',1)]):
	print test,(test['time']+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),'\n'

# 1.limit()方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。
# 2.使用skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。
# 3.limit结合skip实现分页：
# db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
# 4.使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而-1是用于降序排列。
# 5.当查询时同时使用sort,skip,limit，无论位置先后，最先执行顺序 sort 再 skip 再 limit。
# 6.skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。
# 7.skip和limit方法只适合小数据量分页，如果是百万级效率就会非常低，因为skip方法是一条条数据数过去的，建议使用where_limit