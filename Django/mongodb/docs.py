# -*- coding:utf-8 -*-
# pymongo的入门训练

import pymongo
from pymongo import MongoClient

# 创建连接mongodb的方式
# 方式一
# client = MongoClient()
# 方式二
# client = MongoClient('localhost',27017)
# 方式三
client = MongoClient('mongodb://localhost:27017')

# 获取数据库
# db = client.test
# 或者类似字典访问
db = client['test']

# 获取集合
# collection = db.posts
# 或者
collection = db['posts']
# 注意上面的数据库或者集合如果事先没有创建好，在后面插入文档数据的时候会自动进行创建的。

import datetime
# 声明一个文档数据dict格式，插入数据库的时候，会自动转换成mongodb认识的数据类型
post = {"author":"Nick","text":"My sencond blog post!","tags":["mongodb", "python", "pymongo"],"date":datetime.datetime.utcnow()}
post_cn = {"author":"Tom","text":"这是我的博客文章!","tags":["mongodb", "python", "pymongo"],"date":datetime.datetime.utcnow()}

# 插入数据
posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# posts.insert_one(post_cn)
# print post_id

# 获取系统中的mongodb指定某个数据库中的集合
# collections = db.collection_names(include_system_collections=False)
# print collections

import pprint
# 查询一个文档数据
pprint.pprint(posts.find_one())
pprint.pprint('-------------')
# 指定条件查询，返回符合查询条件的一个文档数据
pprint.pprint(posts.find_one({"author":"Nick"}))

# 查询不存在的数据，返回None
pprint.pprint(posts.find_one({"author":"Eliot"})) # Nones

print '-------------'

# 通过字符串类型_id查询
post_id = '5a744b834c7e3629e42d12f5'
pprint.pprint(posts.find_one({'_id':post_id})) #None

print '-------------'
# 转换字符串_id成ObjectId类型的_id才可以查询出结果
from bson.objectid import ObjectId
post_id_convert = ObjectId(post_id)
pprint.pprint(posts.find_one({'_id':post_id_convert})) #None
# 注意：在web应用中，通过url传递过来的一些查询参数id如果是字符串，需要通过bson.objectid.ObjectId进行转换成mongodb认识的类型进行查询。


# 批量插入数据
# new_posts = [{
# 	"author":"Mike",
# 	"text": "Another post!",
# 	"tags": ["bulk", "insert"],
# 	"date": datetime.datetime(2009, 11, 12, 11, 14)
# },{
# 	"author": "Eliot",
# 	"title": "MongoDB is fun",
# 	"text": "and pretty easy too!",
# 	"date": datetime.datetime(2009, 11, 10, 10, 45)
# }]
# result = posts.insert_many(new_posts)
# print result.inserted_ids #返回一个ObjectId列表
# 注意：mongodb可以进行动态字段添加，即是有一些document没有这些字段数据，但是也会默认为空。

# 统计总数
print db.posts.count()

# 重复性插入同一个数据对象，只能插入一次，后面将会报错
# doc = {}
# posts.insert_many(doc for _ in range(10))


# 批量查询
postList = posts.find()
for post in postList:
	pprint.pprint(post)
print '-------------'
# 批量查询指定条件的数据
postList2 = posts.find({'author':'Mike'})
for post in postList2:
	pprint.pprint(post)

# 将符合条件的数据进行数目统计
print posts.find({'author':'Mike'}).count()


# 高级查询
print u'......高级查询.....'
d = datetime.datetime(2009,11,12,12)
# 查询出日期小于2009.11.12 12分的数据并按照名字升序输出
for post in posts.find({"date":{'$lt':d}}).sort("author"):
	pprint.pprint(post)

# 建立索引，保持数据的唯一性
print '....index....'
# 创建索引的同时集合也创建好了，使用db.collection.create_index([(<key and index type specification>)], <options> )创建
result = db.profiles.create_index([('user_id',pymongo.ASCENDING)],unique=True)
print result
print sorted(list(db.profiles.index_information()))

# user_profiles = [
# 	{'user_id':211,'name':'Luke'},
# 	{'user_id':212,'name':'Ziltoid'},
# ]
# db.profiles.insert_many(user_profiles)

# 重复添加已经存在的数据
new_profile = {'user_id':213,'name':'Drew'}
duplicate_profile = {'user_id':212,'name':'Tommy'}
result = db.profiles.insert_one(new_profile) #成功添加
result = db.profiles.insert_one(duplicate_profile) #失败，重复的user_id报错
