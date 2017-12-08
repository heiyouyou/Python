# coding=utf-8
import json

# 序列化
d = dict(name='Bob',age=20,score=88)
d_str = json.dumps(d)
print d_str
print type(d_str)
f = open('F:\Python\example\day15\json.txt','wb')
json.dump(d,f)
f.close()

# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
format_json = json.loads(json_str)
print format_json
print type(format_json)
f1 = open('F:\Python\example\day15\json.txt','rb')
format_json1 = json.load(f1, 'utf-8')
print format_json1 #{u'age': 20, u'score': 88, u'name': u'Bob'}
f1.close()

# 反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。